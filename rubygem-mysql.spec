%define rname mysql
%define name ruby-%{rname}
%define version 2.8.1
%define release %mkrel 9

Summary:    This is the MySQL API module for Ruby
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://mysql-win.rubyforge.org
Source0: http://rubygems.org/gems/%{rname}-%{version}.gem
License: Ruby License
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: rubygems
Requires: ruby(abi) = 1.8
Suggests: rubygem(hoe) >= 2.3.3
BuildRequires: rubygems
BuildRequires: ruby-devel mysql-devel
Provides: rubygem(%{rname}) = %{version}

%description
This is the MySQL API module for Ruby.
It provides the same functions for Ruby programs that the MySQL C API
provides for C programs.

This is a conversion of tmtm's original extension into a proper RubyGems.

%prep
%setup -q
tar xmf data.tar.gz

%build
%gem_build

%install
rm -rf %buildroot
%gem_install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %{ruby_gemdir}/gems/%{rname}-%{version}/
%{ruby_gemdir}/gems/%{rname}-%{version}/lib
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%doc %{ruby_gemdir}/gems/%{rname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{rname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{rname}-%{version}/README.txt
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
%{ruby_sitearchdir}/mysql_api.so
