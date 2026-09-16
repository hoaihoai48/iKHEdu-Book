from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

p_bullet = parse_xml(f'''
<w:p {nsdecls("w")}>
    <w:pPr>
        <w:pStyle w:val="Compact"/>
        <w:numPr>
            <w:ilvl w:val="0"/>
            <w:numId w:val="9"/>
        </w:numPr>
        <w:spacing w:line="276" w:lineRule="auto"/>
        <w:jc w:val="both"/>
    </w:pPr>
    <w:r><w:t>Dòng 1: Một số nguyên dương</w:t></w:r>
</w:p>
''')
print("Bullet XML valid:", p_bullet.tag)
