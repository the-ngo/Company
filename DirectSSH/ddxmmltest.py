#!/usr/bin/env python

# This script demonstrates the SSHClientInteraction class in the paramiko
# expect library
#
import traceback
import paramiko
from paramiko_expect import SSHClientInteraction

def main():
    # # Set login credentials and the server prompt
    # HOSTNAME = '5.208.16.26'
    # USERNAME = 'NUPADM'
    # PASSWORD = 'ALLPASSW'
    # PROMPT = '< \x08 '
    # # Use SSH client to login
    # try:
    #     # Create a new SSH client object
    #     client = paramiko.SSHClient()
    #
    #     # Set SSH key parameters to auto accept unknown hosts
    #     client.load_system_host_keys()
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     # Connect to the host
    #     client.connect(hostname=HOSTNAME, username=USERNAME, password=PASSWORD)
    #     # Create a client interaction class which will interact with the host
    #     with SSHClientInteraction(client, timeout=10, display=True) as interact:
    #         interact.expect(PROMPT)
    #         interact.send('IFO:OMU:MEASUR:;')
    #         interact.expect(PROMPT)
    #         cmd_output_uname = interact.current_output_clean
    #         interact.send('exit')
    #     print(cmd_output_uname)
    #
    # except Exception:
    #     traceback.print_exc()
    # finally:
    #     try:
    #         client.close()
    #     except:
    #         pass

    import argparse

    parser = argparse.ArgumentParser()

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-n', '--node', nargs='+', help="Designate node to interrogate", required=True, type=str)
    parser.add_argument('-c', '--command', nargs='+', help="Pass a query to the script", required=True, type=str)
    parser.add_argument('-y', '--confirm', help="Confirm execution if prompted", required=False, action="store_true")
    args = parser.parse_args()


if __name__ == '__main__':
    main()