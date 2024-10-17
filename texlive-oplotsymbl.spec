Name:		texlive-oplotsymbl
Version:	44951
Release:	2
Summary:	Some symbols which are not easily available
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oplotsymbl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oplotsymbl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oplotsymbl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is named oPlotSymbl and it includes symbols, which
are not easily available. Especially, these symbols are used in
scientific plots, but the potential user is allowed to use them
in other ways. This package uses TikZ and xcolor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/oplotsymbl
%doc %{_texmfdistdir}/doc/latex/oplotsymbl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
