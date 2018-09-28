# @author Derek Zhang
# downloads the file for bee trajectory

import getpass

thingy = getpass.getpass()
# print(thingy)

import synapseclient
syn = synapseclient.Synapse()

syn.login('derekzhang', thingy)
entity = syn.get('syn11737848', downloadLocation='/Volumes/GoogleDrive/My Drive/public')
print(entity)