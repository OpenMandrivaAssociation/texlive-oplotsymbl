%global tl_name oplotsymbl
%global tl_revision 44951

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Some symbols which are not easily available
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oplotsymbl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oplotsymbl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oplotsymbl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is named oPlotSymbl and it includes symbols, which are not
easily available. Especially, these symbols are used in scientific
plots, but the potential user is allowed to use them in other ways. This
package uses TikZ and xcolor.

