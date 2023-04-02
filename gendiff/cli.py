import json

def generate_diff(filename1, filename2):
	with open('tests/file1.json') as json_file:
		filename1 = json.load(json_file)
	with open('tests/file2.json') as json_file:
		filename2 = json.load(json_file)
	print('{')
	result = {}
	for key in filename1:
		if (key in filename2) and filename2[key] == filename1[key]:
			result['  ' + key] = filename1[key]
			del filename2[key]
		elif (key in filename2) and filename2[key] != filename1[key]:
			result['- ' + key] = filename1[key]
			result['+ ' + key] = filename2[key]
			del filename2[key]
		else:
			result['- ' + key] = filename1[key]
	filename2_reduction = {f'+ {key}': v for key, v in filename2.items()}
	result.update(filename2_reduction)
	result = dict(sorted(result.items(), key=lambda x: x[0][2]))
	for key in result:
		print(key,':', result[key])
	print('}')

if __name__ == '__main__':
    generate_diff(filename1, filename2)
