%-- 4/3/2017 5:49 PM --%
imread("C:\Users\sreejay\Desktop\problem\problem\Defect.png")
imread('Defect.png')
A = imread('Defect.png')
image(A)
B = imread('Defect.png', 'PixelRegion',{[160:700],[ 70:750]})
B = imread('Defect.png', 'PixelRegion',{[160:700],[70:750]})
B = imread('Defect.png', 'PixelRegion',{[160,700],[70,750]})
imhist(A)
figure,imhist(A)
image(A)
B = imread(A, 'PixelRegion',{[160,700],[70,750]})
imcrop(A)
imread(a)
imread(A)
imread(A.png)
B = imcrop(A)
image(B)
figure, imhist(B)
igray = rgb2gray(B)
imshow(Igray)
imshow(igray)
level = .67
Ithresh = im2bw(igray,level)
imshowpair(B,Ithresh,'x')
imshowpair(B,Ithresh,'montage')
Ithresh = im2bw(igray,.8)
imshowpair(B,Ithresh,'montage')
imshowpair(Ithresh,'montage')
imshow(Ithresh)
icom = imcomplement(Ithresh)
Ifilled = imfill(icomp,''holes')
Ifilled = imfill(icomp,'holes')
Ifilled = imfill(icom,'holes')
figure,imshow(Ifilled)
imshow(Ithresh)
Ifilled = imfill(Ithresh,'holes')
figure,imshow(Ifilled)
st = strel('Disk', 75)
75
%%
st = strel('Disk', 75)
Iopen = imopen(Ifilled,st)
imshow(Iopenned)
imshow(Iopen)
st = strel('Disk', 25)
Iopen = imopen(Ifilled,st)
imshow(Iopenned)
imshow(Iopen)
st = strel('Disk', 5)
Iopen = imopen(Ifilled,st)
imshow(Iopen)
imshow(Ithresh)
imshow(Ifilled)
imshow(Ithresh)
figure,imshow(Ifilled)
imshow(Iopen)
figure2,imshow(Iopen)
figure,imshow(Iopen)
figure,imshow(Ifilled)
Iregion = regionprops(Iopen, 'Area')
[labeled,numObjects] = bwlabel(Iopen,4)
stats = regionprops(labeled,'Area')
areas = [stats.Area]
areas =
139512         106         324
imshow(106)
%-- 4/3/2017 5:49 PM --%
imread("C:\Users\sreejay\Desktop\problem\problem\Defect.png")
imread('Defect.png')
A = imread('Defect.png')
image(A)
B = imread('Defect.png', 'PixelRegion',{[160:700],[ 70:750]})
B = imread('Defect.png', 'PixelRegion',{[160:700],[70:750]})
B = imread('Defect.png', 'PixelRegion',{[160,700],[70,750]})
imhist(A)
figure,imhist(A)
image(A)
B = imread(A, 'PixelRegion',{[160,700],[70,750]})
imcrop(A)
imread(a)
imread(A)
imread(A.png)
B = imcrop(A)
image(B)
figure, imhist(B)
igray = rgb2gray(B)
imshow(Igray)
imshow(igray)
level = .67
Ithresh = im2bw(igray,level)
imshowpair(B,Ithresh,'x')
imshowpair(B,Ithresh,'montage')
Ithresh = im2bw(igray,.8)
imshowpair(B,Ithresh,'montage')
imshowpair(Ithresh,'montage')
imshow(Ithresh)
icom = imcomplement(Ithresh)
Ifilled = imfill(icomp,''holes')
Ifilled = imfill(icomp,'holes')
Ifilled = imfill(icom,'holes')
figure,imshow(Ifilled)
imshow(Ithresh)
Ifilled = imfill(Ithresh,'holes')
figure,imshow(Ifilled)
st = strel('Disk', 75)
75
%%
st = strel('Disk', 75)
Iopen = imopen(Ifilled,st)
imshow(Iopenned)
imshow(Iopen)
st = strel('Disk', 25)
Iopen = imopen(Ifilled,st)
imshow(Iopenned)
imshow(Iopen)
st = strel('Disk', 5)
Iopen = imopen(Ifilled,st)
imshow(Iopen)
imshow(Ithresh)
imshow(Ifilled)
imshow(Ithresh)
figure,imshow(Ifilled)
imshow(Iopen)
figure2,imshow(Iopen)
figure,imshow(Iopen)
figure,imshow(Ifilled)
Iregion = regionprops(Iopen, 'Area')
[labeled,numObjects] = bwlabel(Iopen,4)
stats = regionprops(labeled,'Area')
areas = [stats.Area]
areas =
139512         106         324
imshow(106)
Ifilled = imfill(Ithresh,'holes')
figure,imshow(Ifilled)
st = strel('Disk', 75)
st = strel('Disk', 71000)
st = strel('Disk', 710)
figure,imshow(Ifilled)
st = strel('Disk', 5)
st = strel('Disk', 150)
Iopen = imopen(Ifilled,st)
figure,imshow(Ifilled)
Iopen = imopen(Ifilled,st)
Imshow(Iopen)
imshow(Iopen)
Iregion = regionprops(Iopen, 'Area')
[labeled,numObjects] = bwlabel(Iopen,4)
stats = regionprops(labeled,'Area')
areas1 = stats.area
areas1 = [stats.Area]
Iregion = regionprops(Iopen, 'Area')
[labeled,numObjects] = bwlabel(Iopen,4)
stats = regionprops(labeled,'Area')
areas1 = stats.area
areas1 = [stats.Area]
Imshow(Iopen)
imshow(Iopen)
Iregion = regionprops(Iopen, 'Area')
[labeled,numObjects] = bwlabel(Iopen,4)
stats = regionprops(labeled,'Area')
areas1 = [stats.Area]
areas
areas[1]
areas[1,1]
areas
st = strel('Disk', 150)
Iopen = imopen(Ifilled,st)
Iopen= imopen(Ifilled,st)
totalarea = sum(areas)
st = strel('Disk', 0)
Iopen = imopen(Ifilled,st)
Imshow(Iopen)
[labeled,numObjects] = bwlabel(Iopen,4)
Iopen
ifilled
Ifilled
st = strel('Disk', 0)
Iopen = imopen(Ifilled,st)
st = strel('Disk', 150)
Iopen = imopen(Ifilled,st)
Iopen
x = imread('Defect.png');
figure
image(x)
idx = all(x==0,3);
x(repmat(idx,[1,1,3]))=255;
figure
image(x)
x = imread('Defect.png');
image(x)
x = imread('Defect.png');
image(x)
idx = all(x==0,3);
x(repmat(idx,[1,1,3]))=255;
figure
image(x)
x = imread('Defect.png');
Imshow(Iopen)
imshow(Iopen)
x = imshow(Iopen)
image(x)
x = imshow(Iopen)
idx = all(x==0,3)
x(repmat(idx,[1,1,3]))=255;
x(repmat(idx,[1,1,3]))=255
x(repmat(idx,[1,1,3]))
y=x(repmat(idx,[1,1,3]))
image[y]
imshow(y)
Ifilled = imfill(Ithresh,'holes')
imshow(iopen)
imshow(Iopen)
bin_im = im2bw(Iopen,graythresh(Iopen))
bin_im = imcomplement(Iopen)
imshow(bin_im)
st = strel('Disk', 5)
Iopen = imopen(bin_im,st)
Iopen
Iregion1 = regionprops(bin_im, 'Area')
areas1 = [stats.Area]
[labeled,numObjects] = bwlabel(Iopen,4)
stats = regionprops(labeled,'Area')
areas1 = [stats.Area]
area
areas
totalarea
x = totalarea/areas1
imshow(x)
imshow(iopen)
imshow(Iopen)