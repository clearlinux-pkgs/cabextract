#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cabextract
Version  : 1.7
Release  : 5
URL      : http://www.cabextract.org.uk/cabextract-1.7.tar.gz
Source0  : http://www.cabextract.org.uk/cabextract-1.7.tar.gz
Summary  : A program to extract Microsoft Cabinet files
Group    : Development/Tools
License  : GPL-3.0
Requires: cabextract-bin
Requires: cabextract-license
Requires: cabextract-man

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program unpacks these files.

%package bin
Summary: bin components for the cabextract package.
Group: Binaries
Requires: cabextract-license
Requires: cabextract-man

%description bin
bin components for the cabextract package.


%package license
Summary: license components for the cabextract package.
Group: Default

%description license
license components for the cabextract package.


%package man
Summary: man components for the cabextract package.
Group: Default

%description man
man components for the cabextract package.


%prep
%setup -q -n cabextract-1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533060700
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1533060700
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cabextract
cp COPYING %{buildroot}/usr/share/doc/cabextract/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cabextract

%files license
%defattr(-,root,root,-)
/usr/share/doc/cabextract/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/cabextract.1
