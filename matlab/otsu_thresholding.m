clc;
clear;
close all;

% Read satellite image
img = imread('input_image.jpg');

% Convert to grayscale if RGB
if size(img,3) == 3
    grayImg = rgb2gray(img);
else
    grayImg = img;
end

% Apply Otsu Thresholding
level = graythresh(grayImg);
binaryImage = imbinarize(grayImg, level);

% Display results
figure;
subplot(1,2,1);
imshow(grayImg);
title('Original Image');

subplot(1,2,2);
imshow(binaryImage);
title('Otsu Thresholding Result');

% Save output
imwrite(binaryImage, 'otsu_output.png');