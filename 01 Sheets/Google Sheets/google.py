from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
# En el siguiente link pueden ver los permisos
# https://developers.google.com/sheets/api/guides/authorizing
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1nJVeRMMGCS-sQCAAcHdc2ZNNLHVdkOlc-HrSD4xeakk'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('credentials/token.json'):
        creds = Credentials.from_authorized_user_file('credentials/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('credentials/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    # Desde aqui es cuando ya se empieza a manipular la planilla
    sheet = service.spreadsheets()

    # hacemos una consulta de datos
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range='A2:E6').execute()
    values = result.get('values', [])

    # revisamos si tenemos datos
    if not values:
        print('No data found.')
    else:
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            # print('%s, %s' % (row[0], row[4]))
            print(row)

    # The A1 notation of the values to update.
    range_ = 'A1:C2'  # TODO: Update placeholder value.

    # How the input data should be interpreted.
    value_input_option = 'USER_ENTERED'
    # value_input_option = 'RAW'

    value_range_body = {
        'values': [
            ['=A2+B2', 'nada', 'jaja3'],
            ['1', '2', 'jaja1']
        ]
    }

    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=range_,
                                                     valueInputOption=value_input_option, body=value_range_body)
    response = request.execute()

    # printiamos la respuesta de la request
    print(response)


if __name__ == '__main__':
    main()
