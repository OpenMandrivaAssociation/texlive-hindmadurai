%global tl_name hindmadurai
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1
Release:	%{tl_revision}.1
Summary:	The HindMadurai font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/hindmadurai
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hindmadurai.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hindmadurai.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the HindMadurai family of fonts designed by the
Indian Type Foundry, with support for LaTeX and pdfLaTeX.

