%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-automotive-autonomy-msgs
Version:        3.0.3
Release:        1%{?dist}
Summary:        ROS automotive_autonomy_msgs package

License:        MIT
URL:            http://github.com/automotive_autonomy_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-automotive-navigation-msgs
Requires:       ros-melodic-automotive-platform-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-ros-environment

%description
Messages for vehicle automation

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Tue Jan 07 2020 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 3.0.3-1
- Autogenerated by Bloom

* Thu Dec 19 2019 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 3.0.2-1
- Autogenerated by Bloom

* Thu Dec 12 2019 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 3.0.1-1
- Autogenerated by Bloom

* Fri Dec 07 2018 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 2.0.3-0
- Autogenerated by Bloom

* Wed Aug 08 2018 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 2.0.2-0
- Autogenerated by Bloom

