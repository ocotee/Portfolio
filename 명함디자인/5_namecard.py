#-*-coding:euc-kr

#??? �� ã�� ä��������

import time
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���������� ����� CSV������ �ҷ��ɴϴ�.
personal_IDs = sys.argv[1]

# ���Կ� ������ �ΰ� ������ �Է¹޽��ϴ�.
logo_filename = sys.argv[2]

# ���Կ� ������ ȸ�� ������ �����մϴ�.
location = "����Ư���� ������ ���ɴ�� 127"
url = "https://bit.ly/2FqKtba"

# ������� ������ ������ �����մϴ�.
out_dir ="namecards"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# �ΰ� ������ �ҷ��ɴϴ�.
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

# ������ �ػ󵵸� �����մϴ�. ���۸� �� ���� 1039*697 ����� �����.
Xdim = 1039
Ydim = 697

# �ΰ� ũ�⸦ ���Կ� �����ϱ� ���� �����մϴ�. ������ ���ΰ� ª���� ���� ���̸� �������� �۾��մϴ�.
# �ΰ��� ���̸� ���� ������ 40%�� �����մϴ�.
new_logo_y = int(Ydim * 0.4)
# �ΰ��� x�� ���̴� ��ʽ����� ����մϴ�.
# new_logo_y : logo_y = new_logo_x : logo_x
# �����մϴ�. �ʵ��б��� �ٵ� ������ϴ�.
new_logo_x = int(logo_x * (new_logo_y / logo_y))

# ���Կ� �����ϱ� ���� �ΰ� ũ�⸦ �����մϴ�.
resized_logo = logo.resize((new_logo_x, new_logo_y))

# ���� �� �ΰ� �ݾ��ݴϴ�. �Ǽ��� ������ �ѼյǴ� ���� �����մϴ�.
logo.close()

# ���������� �ҷ��ɴϴ�.
IDs = open(personal_IDs)

# ����� �̾Ƴ��ϴ�.
header = IDs.readline()

# ������ ������ ���ο� �̹����� ������ �ݴϴ�.
# ����� ������ �ϴ� ������� �����սô�.
# ������ õ �� ���̳� ���� �� ȸ��� �ӿ��� ������ �������� ���ɼ��� ������
# �� ���� �ƴ� �ٸ� ������ ���Ѵ� �ϴ��� ����� �ƴ� �ٸ� �� ���̿� �μ��ϸ� �˴ϴ�.
image = Image.new("RGBA", (Xdim, Ydim), "white")

# �� ���� �»�ܿ� �ΰ� �����ϰڽ��ϴ�.
# ���� ������ 10%���� �ָ� �����ϰ���? �̰� �������� ���⿡ �޷� �ֽ��ϴ�.
image.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.1)),resized_logo)

# �ΰ� �ݾ��ݴϴ�. �޸� ��뷮�� �ٿ��ݴϴ�.
resized_logo.close()

# ���Կ� ������ ��Ʈ���� �����մϴ�.
# ��Ʈ �̸��� �����Ͻø� �ٲ�ϴ�. �⺻�� �����Դϴ�. ��ǻ�͸� �� ������ �����Դϴ�.
# �̸��� ū ���ڷ� �����սô�.
nameFont = ImageFont.truetype("font/gulim.ttc", 70)
# URL�� �ּҴ� ������ �۰� �����Ұ̴ϴ�.
smallFont = ImageFont.truetype("font/gulim.ttc", 40)
# ������ �������� ������ ũ��� �ۼ��մϴ�.
infoFont = ImageFont.truetype("font/gulim.ttc", 50)

# ���� ���� �ֻ�ܿ� URL�� �����մϴ�.
# �¿� ������ �� ���� 5%�� ���̴ϴ�.
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
# ��� ������ 5%������ ����� �� �����ϴ�.
y_offset = int(Ydim * 0.05)
# ���Կ� Ȩ������ �ּҸ� �����մϴ�.
ImageDraw.Draw(image).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")

# ���� �ϴܿ� �繫�� �ּҸ� �Է��մϴ�.
# �¿� ������ ���� 5%�� ���̴ϴ�.
x_offset = int(Xdim * 0.95 - smallFont.getsize(location)[0])
# �ϴ� ���鵵 ���������� 5%������ ���� �� ������.
y_offset = int(Ydim * 0.95 - smallFont.getsize(location)[1])
# ���Կ� �繫�� �ּҸ� �����մϴ�.
ImageDraw.Draw(image).text(xy=(x_offset, y_offset), text=location, font=smallFont, fill="black")

# ���������� ���پ� �о���鼭, �� ���� ������ �� �徿 ����̴ϴ�.
for line in IDs:
    # CSV�ϱ� �ĸ� ������ �ɰ� �� �ֽ��ϴ�. �ɰ��ô�.
    splt = line.strip().split(",")

    # ���Կ� �� �����鸸 �����մϴ�.
    name = splt[0]
    e_mail = splt[2]
    division = splt[3]
    telephone = splt[4]

    # ���� ���ø��� �����մϴ�.
    namecard = image.copy()

    # �̸��� �����Ұ̴ϴ�.
    # �̸� ���̻��� ������ �����ؼ� �� �� ���̰� �մϴ�.
    temp_name = ""
    for el in name:
        temp_name += el + " "
    name = temp_name[:-1]
    # �̸��� ���� ������ 10% �ݽô�.
    x_offset = int(Xdim * 0.9 - nameFont.getsize(name)[0])
    # ���� ������ 60%�� �ݽô�.
    y_offset = int(Ydim * 0.4 - nameFont.getsize(name)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # �̸� �ؿ� �μ����� �����Ұ̴ϴ�.
    # �μ��� ���� ������ 10% �ݽô�.
    x_offset = int(Xdim * 0.9 - infoFont.getsize(division)[0])
    # ���� ������ 50%�� �ݽô�.
    y_offset = int(Ydim * 0.5 - infoFont.getsize(division)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=division, font=infoFont, fill="black")

    # �� �ؿ� ��ȭ��ȣ�� �����Ұ̴ϴ�.
    # ���� ������ 10% �ݽô�.
    x_offset = int(Xdim * 0.9 - infoFont.getsize(telephone)[0])
    # ���� ������ 35%�� �ݽô�.
    y_offset = int(Ydim * 0.65 - infoFont.getsize(telephone)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=telephone, font=infoFont, fill="black")

    # �� �ؿ� �̸����� �����Ұ̴ϴ�.
    # ���� ������ 10% �ݽô�.
    x_offset = int(Xdim * 0.9 - infoFont.getsize(e_mail)[0])
    # ���� ������ 25%�� �ݽô�.
    y_offset = int(Ydim * 0.75 - infoFont.getsize(e_mail)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=e_mail, font=infoFont, fill="black")

    # �ϼ��� ������ �����մϴ�.
    namecard.save(out_dir + "/" + division + "_" + name + "_" + telephone + ".png")

    # ���嵵 ������ ������ �ݾ��ݴϴ�.
    namecard.close()

# ���ø��� �ݾ��ݴϴ�.
image.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
