# Generated from mysql-2.8.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	mysql

Summary:	This is the MySQL API module for Ruby
Name:		rubygem-%{rbname}

Version:	2.8.1
Release:	9
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://mysql-win.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel mysql-devel
%rename		ruby-mysql

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(extra|tasks|test)'

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/extra
%{ruby_gemdir}/gems/%{rbname}-%{version}/extra/*.css
%{ruby_gemdir}/gems/%{rbname}-%{version}/extra/*.html
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*.rake
%{ruby_sitearchdir}/mysql_api.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb


%changelog
* Thu Feb 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.8.1-9
+ Revision: 774808
- rename from ruby-mysql to rubygem-mysql
- regenerate spec with gem2rpm5

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.8.1-9
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-8
+ Revision: 645878
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-7mdv2011.0
+ Revision: 627286
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-6mdv2011.0
+ Revision: 626560
- rebuilt against mysql-5.5.8 libs

* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 2.8.1-4mdv2011.0
+ Revision: 623457
- Package as a gem
- fix License
- fix Requires
- use %%gem_macros
- update file list
- update URLs

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-3mdv2011.0
+ Revision: 614744
- the mass rebuild of 2010.1 packages

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-2mdv2010.1
+ Revision: 507508
- rebuild

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 2.8.1-1mdv2010.0
+ Revision: 402813
- update to new version 2.8.1

* Thu Jan 01 2009 Funda Wang <fwang@mandriva.org> 2.8-2mdv2009.1
+ Revision: 323120
- update license

* Thu Jan 01 2009 Funda Wang <fwang@mandriva.org> 2.8-1mdv2009.1
+ Revision: 323080
- New version 2.8

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.7.6-2mdv2009.1
+ Revision: 311343
- rebuilt against mysql-5.1.30 libs

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 2.7.6-1mdv2009.0
+ Revision: 280667
- New Release

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.7.1-2mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 2.7.1-2mdv2008.0
+ Revision: 16895
- Use Development/Ruby group
- Use std macros


* Sat Jun 10 2006 Pascal Terjan <pterjan@mandriva.org> 2.7.1-1mdv2007.0
- New release 2.7.1
- Add URL in Source

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 2.7-2mdk
- rebuilt against MySQL-5.0.15

* Fri Sep 02 2005 Pascal Terjan <pterjan@mandriva.org> 2.7-1mdk
* Tue Aug 02 2005 Pascal Terjan <pterjan@mandrake.org> 2.6.3-1mdk
- 2.6.3

* Tue Apr 26 2005 Pascal Terjan <pterjan@mandrake.org> 2.6-1mdk
- 2.6.1

* Fri Apr 01 2005 Pascal Terjan <pterjan@mandrake.org> 2.5-3mdk
- lib64 fix

* Thu Feb 10 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.5-2mdk
- rebuilt against new mysql libs

* Wed Sep 08 2004 Pascal Terjan <pterjan@mandrake.org> 2.5-1mdk 
- first mdk release

