
%define	rbname	mysql

Summary:	This is the MySQL API module for Ruby
Name:		rubygem-%{rbname}

Version:	2.9.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://mysql-win.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel 
BuildRequires:	mysql-devel

# keep this please .Sflo
%if %{mdvver} >= 201410
Provides:	rubygem-mariadb
%endif

%rename		ruby-mysql

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.

%files
%{gem_dir}/gems/%{rbname}-%{version}/extra/*.css
%{gem_dir}/gems/%{rbname}-%{version}/extra/*.html
%{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/gems/%{rbname}-%{version}/tasks/*.rake
%{ruby_sitearchdir}/mysql/mysql_api.so
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
#-----------------------------------------------------------

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/*.txt
%{gem_dir}/gems/%{rbname}-%{version}/test/*.rb
#-----------------------------------------------------------

%prep
%setup -q

%build
%gem_build -f '(extra|tasks|test)'

%install
%gem_install

rm -fr %{buildroot}%{gem_dir}/gems/%{rbname}-%{version}/.gemtest
perl -pi -e "s|/usr/local/bin/ruby|/usr/bin/ruby|" %{buildroot}%{gem_dir}/gems/%{rbname}-%{version}/test/test_mysql.rb
chmod +x %{buildroot}%{gem_dir}/gems/%{rbname}-%{version}/test/test_mysql.rb




