from bs4 import BeautifulSoup
html_data = """
<ul>
<li><a href="https://fuckingfast.co/jypnrk04cbte#RDR2_Updated_Setup_Files.part1.rar" target="_blank" rel="nofollow noopener noreferrer">https://fuckingfast.co/jypnrk04cbte#RDR2_Updated_Setup_Files.part1.rar</a></li>
<li><a href="https://fuckingfast.co/q7iokp6a8l9e#RDR2_Updated_Setup_Files.part2.rar" target="_blank" rel="nofollow noopener noreferrer">https://fuckingfast.co/q7iokp6a8l9e#RDR2_Updated_Setup_Files.part2.rar</a></li>
<li><a href="https://fuckingfast.co/x5s0a4s4knsn#RDR2_Updated_Setup_Files.part3.rar" target="_blank" rel="nofollow noopener noreferrer">https://fuckingfast.co/x5s0a4s4knsn#RDR2_Updated_Setup_Files.part3.rar</a></li>
<li><a href="https://fuckingfast.co/v4mu90lqq136#RDR2_Updated_Setup_Files.part4.rar" target="_blank" rel="nofollow noopener noreferrer">https://fuckingfast.co/v4mu90lqq136#RDR2_Updated_Setup_Files.part4.rar</a></li>
<li><a href="https://fuckingfast.co/6z9g0iw5dkq0#RDR2_Updated_Setup_Files.part5.rar" target="_blank" rel="nofollow noopener noreferrer">https://fuckingfast.co/6z9g0iw5dkq0#RDR2_Updated_Setup_Files.part5.rar</a></li>
<li><a href="https://fuckingfast.co/56bwe31rwpjs#RDR2_Updated_Setup_Files.part6.rar" target="_blank" rel="nofollow noopener noreferrer">https://fuckingfast.co/56bwe31rwpjs#RDR2_Updated_Setup_Files.part6.rar</a></li>
</ul>
"""

# Parse the HTML
soup = BeautifulSoup(html_data, 'html.parser')

# Extract hrefs into a list
url_list = [a['href'] for a in soup.find_all('a', href=True)]
