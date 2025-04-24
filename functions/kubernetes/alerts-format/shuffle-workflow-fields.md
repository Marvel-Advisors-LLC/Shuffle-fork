**Important:** For these fields to work, ensure that you name your nodes in the Shuffle diagram exactly as shown in the image named 'diagram.png,' located in this folder.

### Case Description:

$create_startnode.all_fields.data.log_message2\n\n
File hash: $create_startnode.all_fields.data.file_hash\n\n
OS: $create_startnode.all_fields.data.operating_system\n\n
Site: $create_startnode.all_fields.data.site_name\n\n
SentinelOne site_id: $create_startnode.all_fields.data.site_id\n\n
Timestamp: $create_startnode.all_fields.timestamp \n\n
Predecoder Hostname: $create_startnode.all_fields.predecoder.hostname\n\n
Location: $create_startnode.all_fields.location\n\n
Rule firedtimes: $create_startnode.all_fields.rule.firedtimes\n\n
Wazuh rule level: $create_startnode.all_fields.rule.level\n\n

### VirusTotal Report:

Meaningful name: $virustotal_v3_1_check_filehash.body.data.attributes.meaningful_name\n\n
Creation date: $virustotal_v3_1_check_filehash.body.data.attributes.creation_date\n\n
First submission: $virustotal_v3_1_check_filehash.body.data.attributes.first_submission_date\n\n
VirusTotal URL: https://www.virustotal.com/gui/file/$virustotal_v3_1_check_filehash.body.data.attributes.sha256/detection\n\n

### Case Name:

Suspicious threat on $create_startnode.all_fields.data.endpoint - Wazuh Rule ID: $create_startnode.all_fields.rule.id
