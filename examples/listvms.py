#!/usr/bin/env python
import json
import azurerm


# Load Azure app defaults
try:
    with open('azurermconfig.json') as configFile:
        configData = json.load(configFile)
except FileNotFoundError:
    print("Error: Expecting vmssConfig.json in current folder")
    sys.exit()

tenant_id = configData['tenantId']
app_id = configData['appId']
app_secret = configData['appSecret']
subscription_id = configData['subscriptionId']
resource_group = configData['resourceGroup']
access_token = azurerm.get_access_token(tenant_id, app_id, app_secret)

# loop through resource groups
resource_groups = azurerm.list_resource_groups(access_token, subscription_id)
#print(resource_groups)
for rg in resource_groups["value"]:
    rgname = rg["name"]
    vmlist = azurerm.list_vms(access_token, subscription_id, rgname)
#    print(vmlist)
    for vm in vmlist['value']:
        name = vm['name']
        #location = vm['location']
        user = vm['properties']['osProfile']['adminUsername']
        #computername = vm['properties']['osProfile']['computerName']
        print(''.join(['Name: ', name,
                       ', RG: ', rgname,
        #               ', location: ', location,
                       ', user: ', user,
        #               ' ComputerName: ', computername]))
                       ]))

# get extension details (note the hardcoded values you'll need to change
#extn = azurerm.get_vm_extension(access_token, subscription_id, resource_group, 'MyDockerVm', 'LinuxDiagnostic')
#print(json.dumps(extn, sort_keys=False, indent=2, separators=(',', ': ')))
