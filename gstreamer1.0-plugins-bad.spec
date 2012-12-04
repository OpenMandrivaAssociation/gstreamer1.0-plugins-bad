%define api		1.0
%define bname		gstreamer%{api}

%define build_experimental	0
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_amrwb	0
%define build_faac	0
%define build_faad	0
%define build_xvid	0
%define build_dts	0
%define build_dirac	0
%define build_gme	1
%define build_celt	1

##########################
# Hardcode PLF build
%define build_plf	0
##########################

%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%define build_amrwb	0
%define build_faac	1
%define build_faad	1
%define build_xvid	0
%define build_dts	1
%endif

%define libmajor	0
%define libnamephoto	%mklibname gstphotography %{api} %{libmajor}
%define develnamephoto	%mklibname -d gstphotographyi %{api}
%define libnamebase	%mklibname gstbasevideo %{api} %{libmajor}
%define develnamebase	%mklibname -d gstbasevideo %{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-bad
Version:	1.0.3
Release:	1%{?extrarelsuffix}
License:	LGPLv2+ and GPLv2+
Group: 		Sound
URL:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Patch0:		gst-plugins-bad-0.10.7-wildmidi-timidity.cfg.patch
# gw: fix for bug #36437 (paths to realplayer codecs)
# prefer codecs from the RealPlayer package in restricted
Patch10:	gst-plugins-bad-0.10.6-real-codecs-path.patch
#gw for the pixbuf plugin
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:	pkgconfig(sdl)
BuildRequires:	libbzip2-devel
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(opus)
%ifarch %ix86
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	pkgconfig(valgrind)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:	pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libmimic)
BuildRequires:	pkgconfig(libass)
%if %{build_plf}
BuildRequires:	pkgconfig(vo-aacenc)
BuildRequires:	pkgconfig(vo-amrwbenc)
%endif
#gw for checks
#BuildRequires:	gstreamer0.10-plugins-good
BuildRequires:	fonts-ttf-dejavu
#gw for autoreconf
BuildRequires:	gettext-devel
Requires:	%{bname}-voip >= %{version}-%{release}

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%package -n %{libnamephoto}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libnamephoto}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %{develnamephoto}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libnamephoto} = %{version}-%{release}
Provides:	gstphotography%{api}-devel = %{version}-%{release}

%description -n %{develnamephoto}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n %{libnamebase}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libnamebase}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %{develnamebase}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libnamebase} = %{version}-%{release}
Provides:	gstbasevideo%{api}-devel = %{version}-%{release}

%description -n %{develnamebase}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n %{bname}-curl
Summary:	GStreamer Curl plugin
Group:		Networking/Other
BuildRequires:	pkgconfig(libcurl)

%description -n %{bname}-curl
This is a HTTP plugin for GStreamer based on the curl library.

%files -n %{bname}-curl
%{_libdir}/gstreamer-%{api}/libgstcurl.so

%package -n %{bname}-mpeg2enc
Summary:	GStreamer mjpegtools plug-in
Group:		Video
BuildRequires:	pkgconfig(mjpegtools)

%description -n %{bname}-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %{bname}-mpeg2enc
%{_libdir}/gstreamer-%{api}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{api}/libgstmplex.so

%if %{build_gme}
%package -n %{bname}-gme
Summary:	GStreamer Game Music plug-in
Group:		Sound
BuildRequires:	libgme-devel

%description -n %{bname}-gme
Game Music decoding plug-in.

%files -n %{bname}-gme
%{_libdir}/gstreamer-%{api}/libgstgme.so
%endif

%if %{build_dirac}
%package -n %{bname}-dirac
Summary:	GStreamer dirac plug-in
Group:		Video
BuildRequires:	pkgconfig(dirac) >= 0.9

%description -n %{bname}-dirac
Dirac encoding and decoding plug-in.

%files -n %{bname}-dirac
%{_libdir}/gstreamer-%{api}/libgstdirac.so
%endif

%package -n %{bname}-schroedinger
Summary:	GStreamer dirac plug-in based on Schroedinger
Group:		Video
BuildRequires:	pkgconfig(schroedinger-1.0)
Epoch:		1

%description -n %{bname}-schroedinger
Dirac encoding and decoding plug-in based on Schroedinger.

%files -n %{bname}-schroedinger
%{_libdir}/gstreamer-%{api}/libgstschro.so

%package -n %{bname}-vp8
Summary:	GStreamer VP8 plug-in
Group:		Video
BuildRequires:	pkgconfig(vpx)

%description -n %{bname}-vp8
VP8 encoding and decoding plug-in.

%files -n %{bname}-vp8
%{_libdir}/gstreamer-%{api}/libgstrtpvp8.so

%if %build_dts
%package -n %{bname}-dts
Summary:	GStreamer plug-ins for DTS audio playback
Group:		Sound
BuildRequires:	dtsdec-devel

%description -n %{bname}-dts
Plug-ins for decoding DTS audio.

%files -n %{bname}-dts
%{_libdir}/gstreamer-%{api}/libgstdtsdec.so
%endif

%if %{build_xvid}
%package -n %{bname}-xvid
Summary:	GStreamer plug-ins for XVID video encoding and decoding
Group:		Video
BuildRequires:	xvid-devel >= 1.1

%description -n %{bname}-xvid
Plug-ins for encoding and decoding XVID video.

This package is in restricted repository as it violates some patents.

%files -n %{bname}-xvid
%{_libdir}/gstreamer-%{api}/libgstxvid.so
%endif

%package -n %{bname}-mms
Summary:	GStreamer plug-in for mms streams
Group:		System/Libraries
Requires:	%{bname}-plugins = %{version}
BuildRequires:	pkgconfig(libmms)

%description -n %{bname}-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %{bname}-mms
%{_libdir}/gstreamer-%{api}/libgstmms.so

%package -n %{bname}-rtmp
Summary:	GStreamer plug-in for rtmp streams
Group:		System/Libraries
Requires:	%{bname}-plugins = %{version}
BuildRequires:	pkgconfig(librtmp)

%description -n %{bname}-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %{bname}-rtmp
%{_libdir}/gstreamer-%{api}/libgstrtmp.so

%package -n %{bname}-soundtouch
Summary:	GStreamer plug-in for SoundTouch support
Group:		Sound
Requires:	%{bname}-plugins = %{version}
BuildRequires:	pkgconfig(soundtouch)

%description -n %{bname}-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %{bname}-soundtouch
%{_libdir}/gstreamer-%{api}/libgstsoundtouch.so

%package -n %{bname}-libass
Summary:	GStreamer subtitles plugin
Group:		Video
BuildRequires:	pkgconfig(libass)

%description -n %{bname}-libass
This is a subtitle plugin for GStreamer based on libass.

%files -n %{bname}-libass
%{_libdir}/gstreamer-%{api}/libgstassrender.so

%package -n %{bname}-voip
Summary:	GStreamer voip plugins
Group:		Sound

%description -n %{bname}-voip
This is a collection of VoIP plugins for GStreamer.

%files -n %{bname}-voip
%{_libdir}/gstreamer-%{api}/libgstrtpmux.so
%{_libdir}/gstreamer-%{api}/libgstdtmf.so

%package doc
Group:		Books/Computer books
Summary:	GStreamer application library
BuildArch:	noarch

%description doc
This is the documentation of %{name}.

%prep
%setup -q -n gst-plugins-bad-%{version}
%apply_patches

%build
%configure2_5x --disable-dependency-tracking --disable-static \
  --with-package-name='Rosa %{name} package' \
  --with-package-origin='http://www.rosalinux.com/' \
%if ! %{build_celt}
	--disable-celt \
%endif
%if ! %{build_faac}
	--disable-faac \
%endif
%if ! %{build_faad}
	--disable-faad \
%endif
%if ! %{build_dirac}
	--disable-dirac \
%endif
%if ! %{build_xvid}
	--disable-xvid \
%endif
%if ! %{build_dts}
	--disable-dts \
%endif
%if ! %{build_plf}
	--disable-voamrwbenc --disable-voaacenc \
%endif
%if %{build_experimental}
	--enable-experimental
%endif

make

%install
%makeinstall_std

%find_lang gst-plugins-bad-%{api}

# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
find %{buildroot} -name '*.la' -delete

%files doc
%doc docs/plugins/html
%{_datadir}/gtk-doc/html/

%files -f gst-plugins-bad-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/gstreamer-%{api}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{api}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{api}/libgstasfmux.so
%{_libdir}/gstreamer-%{api}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{api}/libgstautoconvert.so
%{_libdir}/gstreamer-%{api}/libgstbayer.so
%{_libdir}/gstreamer-%{api}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{api}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{api}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{api}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{api}/libgstdvb.so
%{_libdir}/gstreamer-%{api}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{api}/libgstdvdspu.so
%{_libdir}/gstreamer-%{api}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{api}/libgstfestival.so
%{_libdir}/gstreamer-%{api}/libgstfrei0r.so
%{_libdir}/gstreamer-%{api}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{api}/libgstgdp.so
%{_libdir}/gstreamer-%{api}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{api}/libgstid3tag.so
%{_libdir}/gstreamer-%{api}/libgstinter.so
%{_libdir}/gstreamer-%{api}/libgstinterlace.so
%{_libdir}/gstreamer-%{api}/libgstjpegformat.so
%{_libdir}/gstreamer-%{api}/libgstliveadder.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{api}/libgstmimic.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{api}/libgstopus.so
%{_libdir}/gstreamer-%{api}/libgstpcapparse.so
%{_libdir}/gstreamer-%{api}/libgstpnm.so
%{_libdir}/gstreamer-%{api}/libgstscaletempoplugin.so
%{_libdir}/gstreamer-%{api}/libgstrawparse.so
%{_libdir}/gstreamer-%{api}/libgstremovesilence.so
%{_libdir}/gstreamer-%{api}/libgstsdpelem.so
%{_libdir}/gstreamer-%{api}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{api}/libgstshm.so
%{_libdir}/gstreamer-%{api}/libgstsiren.so
%{_libdir}/gstreamer-%{api}/libgstsmooth.so
%{_libdir}/gstreamer-%{api}/libgstspeed.so
%{_libdir}/gstreamer-%{api}/libgstsubenc.so
%{_libdir}/gstreamer-%{api}/libgstbz2.so
%{_libdir}/gstreamer-%{api}/libgstfragmented.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{api}/libgstvideoparsersbad.so
%if %{build_plf}
%{_libdir}/gstreamer-%{api}/libgstvoaacenc.so
%{_libdir}/gstreamer-%{api}/libgstvoamrwbenc.so
%{_datadir}/gstreamer-%{api}/presets/GstVoAmrwbEnc.prs
%endif
%if %{build_experimental}
#%{_libdir}/gstreamer-%{api}/libgstdeinterlace2.so
%endif

%{_libdir}/gstreamer-%{api}/libgstmodplug.so
%{_libdir}/gstreamer-%{api}/libgsty4mdec.so

%if %{build_faad}
%package -n %{bname}-faad
Summary:	GStreamer plug-in for AAC audio playback
Group:		Sound
Requires:	%{bname}-plugins >= %{version}
BuildRequires:	libfaad2-devel

%description -n %{bname}-faad
Plug-ins for playing AAC audio

This package is in restricted repository as it violates some patents.

%files -n %{bname}-faad
%{_libdir}/gstreamer-%{api}/libgstfaad.so
%endif

%if %{build_faac}
%package -n %{bname}-faac
Summary:	GStreamer plug-ins for AAC audio encoding
Group:		Sound
Requires:	%{bname}-plugins >= %{version}
BuildRequires:	libfaac-devel

%description -n %{bname}-faac
Plug-ins for encoding AAC audio

This package is in restricted repository as it violates some patents.

%files -n %{bname}-faac
%{_libdir}/gstreamer-%{api}/libgstfaac.so
%endif

%package -n %{bname}-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Group:		Sound
Requires:	%{bname}-plugins >= %{version}
BuildRequires:	gsm-devel >= 1.0.10

%description -n %{bname}-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%files -n %{bname}-gsm
%{_libdir}/gstreamer-%{api}/libgstgsm.so

%if 0
### SWFDEC FLASH PLUGIN ###
%package -n %{bname}-swfdec
Summary: 	GStreamer Flash rendering plug-in
Group:		System/Libraries
Requires:	%{bname}-plugins = %{version}
BuildRequires:	libswfdec-devel => 0.3.0

%description -n %{bname}-swfdec
Plug-in for rendering Flash animations using swfdec library

%files -n %{bname}-swfdec
%{_libdir}/gstreamer-%{api}/libgstswfdec.so
%endif

%if %{build_amrwb}
%package -n %{bname}-amrwb
Summary:	GStreamer plug-in for AMR-WB support
Group:		Sound
Requires:	%{bname}-plugins >= %{version}
BuildRequires:	libamrwb-devel

%description -n %{bname}-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in restricted repository as it violates some patents.

%files -n %{bname}-amrwb
%{_datadir}/gstreamer-%{api}/presets/GstAmrwbEnc.prs
%{_libdir}/gstreamer-%{api}/libgstamrwbenc.so
%endif

%if %{build_celt}
%package -n %{bname}-celt
Summary:	GStreamer plug-in for CELT support
Group:		Video
Requires:	%{bname}-plugins >= %{version}
BuildRequires:	pkgconfig(celt) >= 0.7.0

%description -n %{bname}-celt
Plug-in for CELT support under GStreamer.

%files -n %{bname}-celt
%{_libdir}/gstreamer-%{api}/libgstcelt.so
%endif

%files -n %{libnamephoto}
%{_libdir}/libgstphotography-%{api}.so.%{libmajor}*
%{_libdir}/libgstsignalprocessor-%{api}.so.%{libmajor}*
%{_libdir}/libgstcodecparsers-%{api}.so.%{libmajor}*

%files -n %{develnamephoto}
%{_libdir}/libgstcodecparsers-%{api}.so
%{_libdir}/libgstphotography-%{api}.so
%{_libdir}/libgstsignalprocessor-%{api}.so
%{_includedir}/gstreamer-%{api}/gst/codecparsers/
%{_includedir}/gstreamer-%{api}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{api}/gst/signalprocessor/gstsignalprocessor.h
%{_includedir}/gstreamer-%{api}/gst/video/
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{api}.pc

%files -n %{libnamebase}
%{_libdir}/libgstbasecamerabinsrc-%{api}.so.%{libmajor}*
%{_libdir}/libgstbasevideo-%{api}.so.%{libmajor}*

%files -n %{develnamebase}
%{_libdir}/libgstbasecamerabinsrc-%{api}.so
%{_libdir}/libgstbasevideo-%{api}.so
%{_includedir}/gstreamer-%{api}/gst/basecamerabinsrc/*
%{_libdir}/pkgconfig/gstreamer-basevideo-%{api}.pc


