Name     : simg-tools
Version  : 8.1.0.r29
Release  : 2
URL      : https://android.googlesource.com/platform/system/core/+archive/android-8.1.0_r29.tar.gz
Source0  : https://android.googlesource.com/platform/system/core/+archive/android-8.1.0_r29.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
BuildRequires: zlib-dev
Patch0: 0001-Fix-include-from-string-to-string.h.patch

%description
No detailed description available

%prep
%setup -q -c
%patch0 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525810608
cd libsparse
g++ -c -o sparse_read.o sparse_read.cpp -Iinclude -I../base/include -lz
g++ -c -o stringprintf.o ../base/stringprintf.cpp -Iinclude -I../base/include
gcc -c -o sparse_crc32.o sparse_crc32.c -Iinclude -I../base/include
gcc -c -o sparse_crc32.o sparse_crc32.c -Iinclude -I../base/include
gcc -c -o backed_block.o backed_block.c -Iinclude -I../base/include
gcc -c -o output_file.o output_file.c -Iinclude -I../base/include
gcc -c -o sparse.o sparse.c -Iinclude -I../base/include
gcc -c -o sparse_err.o sparse_err.c -Iinclude -I../base/include
gcc -c -o simg2img.o simg2img.c -Iinclude -I../base/include
gcc -c -o append2simg.o append2simg.c -Iinclude -I../base/include
gcc -c -o img2simg.o img2simg.c -Iinclude -I../base/include
gcc -c -o simg2simg.o simg2simg.c -Iinclude -I../base/include
g++ -o simg2img simg2img.o sparse_crc32.o backed_block.o output_file.o sparse.o sparse_err.o sparse_read.o stringprintf.o -lz
g++ -o append2simg append2simg.o sparse_crc32.o backed_block.o output_file.o sparse.o sparse_err.o sparse_read.o stringprintf.o -lz
g++ -o img2simg -Iinclude img2simg.o sparse_crc32.o backed_block.o output_file.o sparse.o sparse_err.o sparse_read.o stringprintf.o -lz
g++ -o simg2simg -Iinclude simg2simg.o sparse_crc32.o backed_block.o output_file.o sparse.o sparse_err.o sparse_read.o stringprintf.o -lz

%install
export SOURCE_DATE_EPOCH=1525810608
rm -rf %{buildroot}
cd libsparse
install -D -m 755 -t %{buildroot}/usr/bin/ simg2img append2simg img2simg simg2simg

%files
%defattr(-,root,root,-)
/usr/bin/append2simg
/usr/bin/img2simg
/usr/bin/simg2img
/usr/bin/simg2simg
