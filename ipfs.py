import requests
import json

# Project ID: 2FTtIoa5G1Q3oWsCYT0fmE8MHPq
# IPFS API Endpoint: https://ipfs.infura.io:5001
# API Key Secret: 2066e379d1f4119e39665ceaadc0eabb
# data: Python Dictionary: key:value

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE

	project_id = '2FTtIoa5G1Q3oWsCYT0fmE8MHPq'
	IPFS_API_endpoint = 'https://ipfs.infura.io:5001'
	project_secret = '2066e379d1f4119e39665ceaadc0eabb'

	files = {
		'file': json.dumps(data)
		}
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=(project_id, project_secret))
	print(response.text)

	cid = response.text.split(",")[1].split(":")[1].replace('"','')
	print (cid)

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	project_id = '2FTtIoa5G1Q3oWsCYT0fmE8MHPq'
	IPFS_API_endpoint = 'https://ipfs.infura.io:5001'
	project_secret = '2066e379d1f4119e39665ceaadc0eabb'

	params = (
		('arg',cid)
	)
	response2 = requests.post('https://ipfs.dev.infura.org:5001/api/v0/cat',params=params, auth=(project_id, project_secret))
	data = response2.json()
	print (data)

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
