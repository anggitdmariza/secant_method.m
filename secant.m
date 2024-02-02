
%Metode secant
syms ('x','x0');
f(x)=input('Fungsi f : '); %menginputlan fungsi 
x0=input('Masukkkan x0 : ');    %menginputkan sebarang titik awal
x1=input('Masukkkan x1 : ');    %menginputkan sebarang titik awal
imax=input('Masukkan iterasi maksimal : '); %menginputkan maksimal iterasi
galat1=input('Masukkan galat toleransi : ');    %menginputkan galat awal

% Membuka file untuk menulis hasil iterasi
fileID = fopen('iterasi_result.txt', 'w');
fprintf(fileID, '      iterasi     akar      f(akar)       galat\n');


for i=1:imax %perintah perulangan 
    x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0));    %rumus metode secant
    galat=abs((x2-x1)/x2); %mencari nilai galat 
    x1=x2; %titik x yang baru diperoleh berubah menjadi titik awal
    y=f(x1); %mendefinisikan y sebagai hasil dari f(x) 
    fprintf('%10.0f    %6.5f    %6.5f    %6.5f\n',[i;x1;y;galat]) %menampilkan iterasi, titik x atau akar, nilai f(x) dan galat
    if (galat<galat1),break,end %ketika salah satu kondisi tercapai, maka proses dihentikan
end

fprintf('Akarnya adalah = %6.5f\n',x1); %menampilkan akar yang diperoleh
% Menutup file
fclose(fileID);