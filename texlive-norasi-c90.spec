Name:		texlive-norasi-c90
Version:	60831
Release:	2
Summary:	TeX support (from CJK) for the norasi font
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-fonts-tlwg

%description
TeXLive norasi-c90 package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/norasi-c90/config.norasi-c90
%{_texmfdistdir}/fonts/map/dvips/norasi-c90/norasi-c90.map
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftnb8z.tfm
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftnbi8z.tfm
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftni8z.tfm
%{_texmfdistdir}/fonts/tfm/public/norasi-c90/ftnr8z.tfm
#- source
%doc %{_texmfdistdir}/source/fonts/norasi-c90/norasi-c90.fontinst

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts source %{buildroot}%{_texmfdistdir}
