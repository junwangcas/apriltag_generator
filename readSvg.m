function [ imageData, width, height ] = readSvg( svgFile )
% 读取 SVG 文件，返回 RGB 图像数据和图像宽度和高度

% 使用 inkscape 将 SVG 转换为 PNG 格式，并读取 PNG 图像数据
system(sprintf('inkscape --export-png=temp.png --export-dpi=300 "%s"', svgFile));
[im, map, alpha] = imread('temp.png');
delete('temp.png');

% 如果有透明度信息，则将透明部分设置为白色
if ~isempty(alpha)
    im = repmat(uint8(255), [size(im, 1), size(im, 2), 1], 'uint8');
    im(:,:,1) = map(im(:,:,1) + 1, 1);
    im(:,:,2) = map(im(:,:,2) + 1, 2);
    im(:,:,3) = map(im(:,:,3) + 1, 3);
end

% 返回 RGB 图像数据和图像宽度和高度
imageData = im;
width = size(im, 2);
height = size(im, 1);


end

