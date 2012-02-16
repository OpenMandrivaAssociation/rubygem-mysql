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
