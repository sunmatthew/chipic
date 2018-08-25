try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string

def writePermutations(string, index, commonMistakes):
	if index + 1 >= len(string):
		newString = string[:index]+commonMistakes[string[index]]
	else:
		newString = string[:index]+commonMistakes[string[index]]+ string[index+1:]
#	file.write(string)
#	file.write("\n")
	permutations = [newString]
	while index >= 0:
		index -= 1
		if string[index] in commonMistakes:
			permutations += writePermutations(string,index,commonMistakes)
			permutations += writePermutations(newString,index,commonMistakes)
			break
	return permutations


def GetStringFromImage(image):
	commonMistakes = {'':''}
	for line in open('CommonReplacements.txt','r'):
		commonMistakes[line[0]] = line[1]
		commonMistakes[line[1]] = line[0]


#	for str in commonMistakes:
#		print(str)
	output = pytesseract.image_to_string(Image.open(image), lang=None, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 8 --load_system_dawg 0 --load_freq_dawg 0')
#	print(output)
#	file = open("testOutput.txt","w")
#	file.write(output)
#	file.write("\n")
	i = len(output)
	while (i >= 0):
		i -= 1;
		if output[i] in commonMistakes:
			return writePermutations(output,i,commonMistakes)
			
# print(GetStringFromImage("test.png"))
#writePermutations(output,len(output))

