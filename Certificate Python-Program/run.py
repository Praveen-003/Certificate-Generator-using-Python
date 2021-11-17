import cv2

list_name = []

def clean_up():
	with open("name-list.txt") as file:
		for line in file:
			list_name.append(line.strip())


def certificate_generated():
	for index, name in enumerate(list_name):
		template = cv2.imread("certificate-template.jpg")
		cv2.putText(template, name, (825, 1500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5, cv2.LINE_AA)
		cv2.imwrite(f'certificate-gernarator data/{name}.jpg',template)
		print(f'{name} {index + 1} / {len(list_name)}')


clean_up()
certificate_generated()