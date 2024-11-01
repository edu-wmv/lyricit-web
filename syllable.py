from bs4 import BeautifulSoup

syllables = open("syllable.xml", "r").read()

ttml = BeautifulSoup(syllables, "html.parser")

syllables = {}
for line in ttml.find_all('p'):
  key = "0" + "".join(filter(str.isdigit, str(line.get("itunes:key"))))
  
  print(key)
  verse = []
  
  if "span" in str(line):
    span = BeautifulSoup(str(line), 'html.parser')
    for s in span.find_all("span", attrs={'begin': True, 'end': True}):
      verse.append(
        {
          "begin": s.get("begin"),
          "end": s.get("end"),
          "text": s.text
        }
      )
    syllables[key] = verse
      