# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-norasi-c90
Version:	20111103
Release:	3
Summary:	TeX support (from CJK) for the norasi font in thailatex
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/norasi-c90.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 754400
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 719131
- texlive-norasi-c90
- texlive-norasi-c90
- texlive-norasi-c90
- texlive-norasi-c90

