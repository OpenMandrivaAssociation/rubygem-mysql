# Generated from mysql-2.8.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	mysql

Summary:	This is the MySQL API module for Ruby
Name:		rubygem-%{rbname}

Version:	2.9.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://mysql-win.rubyforge.org
Source0:	http://rubygems.org/gems/mysql-2.9.1.gem
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
%{ruby_sitedir}/mysql/mysql_api.so
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/History_txt.html
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/Manifest_txt.html
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/Mysql.html
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/Mysql/GemVersion.html
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/README_txt.html
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts.css
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts/Lato-Light.ttf
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts/Lato-LightItalic.ttf
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts/Lato-Regular.ttf
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts/Lato-RegularItalic.ttf
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts/SourceCodePro-Bold.ttf
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/fonts/SourceCodePro-Regular.ttf
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/add.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/arrow_up.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/brick.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/brick_link.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/bug.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/bullet_black.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/bullet_toggle_minus.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/bullet_toggle_plus.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/date.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/delete.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/find.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/loadingAnimation.gif
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/macFFBgHack.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/package.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/page_green.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/page_white_text.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/page_white_width.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/plugin.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/ruby.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/tag_blue.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/tag_green.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/transparent.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/wrench.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/wrench_orange.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/images/zoom.png
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/index.html
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/js/darkfish.js
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/js/jquery.js
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/js/navigation.js
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/js/search.js
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/js/search_index.js
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/js/searcher.js
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/rdoc.css
%{_datadir}/gems/doc/mysql-2.9.1/rdoc/table_of_contents.html
%{_datadir}/gems/doc/mysql-2.9.1/ri/Mysql/GemVersion/cdesc-GemVersion.ri
%{_datadir}/gems/doc/mysql-2.9.1/ri/Mysql/cdesc-Mysql.ri
%{_datadir}/gems/doc/mysql-2.9.1/ri/cache.ri
%{_datadir}/gems/doc/mysql-2.9.1/ri/page-History_txt.ri
%{_datadir}/gems/doc/mysql-2.9.1/ri/page-Manifest_txt.ri
%{_datadir}/gems/doc/mysql-2.9.1/ri/page-README_txt.ri
%{_datadir}/gems/gems/mysql-2.9.1/.gemtest
%{_datadir}/gems/gems/mysql-2.9.1/History.txt
%{_datadir}/gems/gems/mysql-2.9.1/Manifest.txt
%{_datadir}/gems/gems/mysql-2.9.1/README.txt
%{_datadir}/gems/gems/mysql-2.9.1/extra/README.html
%{_datadir}/gems/gems/mysql-2.9.1/extra/README_ja.html
%{_datadir}/gems/gems/mysql-2.9.1/extra/tommy.css
%{_datadir}/gems/gems/mysql-2.9.1/lib/mysql.rb
%{_datadir}/gems/gems/mysql-2.9.1/lib/mysql/version.rb
%{_datadir}/gems/gems/mysql-2.9.1/tasks/gem.rake
%{_datadir}/gems/gems/mysql-2.9.1/tasks/native.rake
%{_datadir}/gems/gems/mysql-2.9.1/tasks/vendor_mysql.rake
%{_datadir}/gems/gems/mysql-2.9.1/test/test_mysql.rb
%{_datadir}/gems/specifications/mysql-2.9.1.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
