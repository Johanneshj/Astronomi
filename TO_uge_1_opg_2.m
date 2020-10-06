clc, clear all, close all

t=linspace(0,24,100);
d1=20;
d2=-10
p=56;

h1 = @(t) asind(sind(d1).*sind(p)+cosd(d1).*cosd(p).*cosd(-90+t.*7.5));
h2 = @(t) asind(sind(d2).*sind(p)+cosd(d2).*cosd(p).*cosd(-90+t.*7.5));

figure(1)
plot(t,h1(t))
figure(2)
plot(t,h2(t))