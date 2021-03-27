from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType
# Import Os
from os import path
import sys
import urllib.request as urreq
import posixpath
from urllib.parse import urlparse as urlp
import requests
import pafy
import humanize
import datetime as dt

# Import UI Design
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), 'main.ui'))


# Initiate Ui Design
class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Buttons()

    def Handel_Ui(self):
        self.setWindowTitle("Media Down")
        self.setFixedSize(610, 380)

    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.Start_Download)
        self.pushButton.clicked.connect(self.Handel_Browse)
        self.pushButton_7.clicked.connect(self.Get_Tube_Video)
        self.pushButton_3.clicked.connect(self.Save_browse)
        self.pushButton_4.clicked.connect(self.Download_Tube_Video)

    # Download File Start

    def Handel_Types(self, file_type):
        """
        :param file_type:
        :return:
        This Is Function Research By
        File Type From Url In Type Dict
        """
        types = {
            'image/svg+xml': '.svg',
            "x-world/x-3dmf": ".3dm",
            "x-world/x-3dmf.copy": ".qd3d",
            "application/octet-stream": ".a",
            "application/x-authorware-bin": ".aab",
            "application/x-authorware-map": ".aam",
            "application/x-authorware-seg": ".aas",
            "text/vnd.abc": ".abc",
            "text/html": ".acgi",
            "video/animaflex": ".afl",
            "application/postscript": ".ai",
            "audio/aiff": ".aif",
            "audio/x-aiff": ".aif",
            "audio/aiff.copy": ".aiff",
            "audio/x-aiff.copy": ".aiff",
            "application/x-aim": ".aim",
            "text/x-audiosoft-intra": ".aip",
            "application/x-navi-animation": ".ani",
            "application/x-nokia-9000-communicator-add-on-software": ".aos",
            "application/mime": ".aps",
            "application/octet-stream.copy": ".zoo",
            "application/arj": ".arj",
            "image/x-jg": ".art",
            "video/x-ms-asf": ".asf",
            "text/x-asm": ".asm",
            "text/asp": ".asp",
            "application/x-mplayer2": ".asx",
            "video/x-ms-asf.copy": ".asx",
            "video/x-ms-asf-plugin": ".asx",
            "audio/basic": ".au",
            "audio/x-au": ".au",
            "application/x-troff-msvideo": ".avi",
            "video/avi": ".avi",
            "video/msvideo": ".avi",
            "video/x-msvideo": ".avi",
            "video/avs-video": ".avs",
            "application/x-bcpio": ".bcpio",
            "application/mac-binary": ".bin",
            "application/macbinary": ".bin",
            "application/x-binary": ".bin",
            "application/x-macbinary": ".bin",
            "image/bmp": ".bm",
            "image/bmp.copy": ".bmp",
            "image/x-windows-bmp": ".bmp",
            "application/book": ".boo",
            "application/book.copy": ".book",
            "application/x-bzip2": ".boz",
            "application/x-bsh": ".bsh",
            "application/x-bzip": ".bz",
            "application/x-bzip2.copy": ".bz2",
            "text/plain": ".c",
            "text/x-c": ".c",
            "text/plain.copy": ".txt",
            "application/vnd.ms-pki.seccat": ".cat",
            "text/x-c.copy": ".cpp",
            "application/clariscad": ".ccad",
            "application/x-cocoa": ".cco",
            "application/cdf": ".cdf",
            "application/x-cdf": ".cdf",
            "application/x-netcdf": ".cdf",
            "application/pkix-cert": ".cer",
            "application/x-x509-ca-cert": ".cer",
            "application/x-chat": ".cha",
            "application/x-chat.copy": ".chat",
            "application/java": ".class",
            "application/java-byte-code": ".class",
            "application/x-java-class": ".class",
            "application/x-cpio": ".cpio",
            "application/mac-compactpro": ".cpt",
            "application/x-compactpro": ".cpt",
            "application/x-cpt": ".cpt",
            "application/pkcs-crl": ".crl",
            "application/pkix-crl": ".crl",
            "application/pkix-cert.copy": ".crt",
            "application/x-x509-ca-cert.copy": ".der",
            "application/x-x509-user-cert": ".crt",
            "application/x-csh": ".csh",
            "text/x-script.csh": ".csh",
            "application/x-pointplus": ".css",
            "text/css": ".css",
            "application/x-director": ".dcr",
            "application/x-deepv": ".deepv",
            "video/x-dv": ".dif",
            "application/x-director.copy": ".dxr",
            "video/dl": ".dl",
            "video/x-dl": ".dl",
            "application/msword": ".doc",
            "application/msword.copy": ".word",
            "application/commonground": ".dp",
            "application/drafting": ".drw",
            "video/x-dv.copy": ".dv",
            "application/x-dvi": ".dvi",
            "drawing/x-dwf (old)": ".dwf",
            "model/vnd.dwf": ".dwf",
            "application/acad": ".dwg",
            "image/vnd.dwg": ".dwg",
            "image/x-dwg": ".dwg",
            "application/dxf": ".dxf",
            "image/vnd.dwg.copy": ".svf",
            "image/x-dwg.copy": ".svf",
            "text/x-script.elisp": ".el",
            "application/x-bytecode.elisp (compiled elisp)": ".elc",
            "application/x-elc": ".elc",
            "application/x-envoy": ".env",
            "application/postscript.copy": ".ps",
            "application/x-esrehber": ".es",
            "text/x-setext": ".etx",
            "application/envoy": ".evy",
            "application/x-envoy.copy": ".evy",
            "text/x-fortran": ".f",
            "text/x-fortran.copy": ".for",
            "application/vnd.fdf": ".fdf",
            "application/fractals": ".fif",
            "image/fif": ".fif",
            "video/fli": ".fli",
            "video/x-fli": ".fli",
            "image/florian": ".flo",
            "text/vnd.fmi.flexstor": ".flx",
            "video/x-atomic3d-feature": ".fmf",
            "image/vnd.fpx": ".fpx",
            "image/vnd.net-fpx": ".fpx",
            "application/freeloader": ".frl",
            "audio/make": ".funk",
            "image/g3fax": ".g3",
            "image/gif": ".gif",
            "video/gl": ".gl",
            "video/x-gl": ".gl",
            "audio/x-gsm": ".gsd",
            "audio/x-gsm.copy": ".gsm",
            "application/x-gsp": ".gsp",
            "application/x-gss": ".gss",
            "application/x-gtar": ".gtar",
            "application/x-compressed": ".gz",
            "application/x-gzip": ".gz",
            "application/x-gzip.copy": ".gzip",
            "multipart/x-gzip": ".gzip",
            "text/x-h": ".h",
            "application/x-hdf": ".hdf",
            "application/x-helpfile": ".help",
            "application/vnd.hp-hpgl": ".hgl",
            "text/x-h.copy": ".hh",
            "text/x-script": ".hlb",
            "application/hlp": ".hlp",
            "application/x-helpfile.copy": ".hlp",
            "application/x-winhelp": ".hlp",
            "application/vnd.hp-hpgl.copy": ".hpgl",
            "application/binhex": ".hqx",
            "application/binhex4": ".hqx",
            "application/mac-binhex": ".hqx",
            "application/mac-binhex40": ".hqx",
            "application/x-binhex40": ".hqx",
            "application/x-mac-binhex40": ".hqx",
            "application/hta": ".hta",
            "text/x-component": ".htc",
            "text/html.copy": ".shtml",
            "text/webviewhtml": ".htt",
            "x-conference/x-cooltalk": ".ice",
            "image/x-icon": ".ico",
            "image/ief": ".ief",
            "image/ief.copy": ".iefs",
            "application/iges": ".iges",
            "model/iges": ".iges",
            "application/iges.copy": ".igs",
            "model/iges.copy": ".igs",
            "application/x-ima": ".ima",
            "application/x-httpd-imap": ".imap",
            "application/inf": ".inf",
            "application/x-internett-signup": ".ins",
            "application/x-ip2": ".ip",
            "video/x-isvideo": ".isu",
            "audio/it": ".it",
            "application/x-inventor": ".iv",
            "i-world/i-vrml": ".ivr",
            "application/x-livescreen": ".ivy",
            "audio/x-jam": ".jam",
            "text/x-java-source": ".jav",
            "text/x-java-source.copy": ".java",
            "application/x-java-commerce": ".jcm",
            "image/jpeg.copy": ".jfif",
            "image/pjpeg.copy": ".jfif",
            "image/jpeg": ".jpg",
            "image/pjpeg": ".jpg",
            "image/x-jps": ".jps",
            "application/x-javascript": ".js",
            "application/javascript": ".js",
            "application/ecmascript": ".js",
            "text/javascript": ".js",
            "text/ecmascript": ".js",
            "image/jutvision": ".jut",
            "audio/midi": ".kar",
            "music/x-karaoke": ".kar",
            "application/x-ksh": ".ksh",
            "text/x-script.ksh": ".ksh",
            "audio/nspaudio": ".la",
            "audio/x-nspaudio": ".la",
            "audio/x-liveaudio": ".lam",
            "application/x-latex": ".latex",
            "application/lha": ".lha",
            "application/x-lha": ".lha",
            "audio/nspaudio.copy": ".lma",
            "audio/x-nspaudio.copy": ".lma",
            "application/x-lisp": ".lsp",
            "text/x-script.lisp": ".lsp",
            "text/x-la-asf": ".lsx",
            "application/x-latex.copy": ".ltx",
            "application/x-lzh": ".lzh",
            "application/lzx": ".lzx",
            "application/x-lzx": ".lzx",
            "text/x-m": ".m",
            "video/mpeg": ".m1v",
            "audio/mpeg": ".m2a",
            "video/mpeg.copy": ".mpg",
            "audio/x-mpequrl": ".m3u",
            "application/x-troff-man": ".man",
            "application/x-navimap": ".map",
            "application/mbedlet": ".mbd",
            "application/x-magic-cap-package-1.0": ".mc$",
            "application/mcad": ".mcd",
            "application/x-mathcad": ".mcd",
            "image/vasa": ".mcf",
            "text/mcf": ".mcf",
            "application/netmc": ".mcp",
            "application/x-troff-me": ".me",
            "message/rfc822": ".mht",
            "message/rfc822.copy": ".mime",
            "application/x-midi": ".mid",
            "audio/midi.copy": ".midi",
            "audio/x-mid": ".mid",
            "audio/x-midi": ".mid",
            "music/crescendo": ".mid",
            "x-music/x-midi": ".mid",
            "application/x-midi.copy": ".midi",
            "audio/x-mid.copy": ".midi",
            "audio/x-midi.copy": ".midi",
            "music/crescendo.copy": ".midi",
            "x-music/x-midi.copy": ".midi",
            "application/x-frame": ".mif",
            "application/x-mif": ".mif",
            "www/mime": ".mime",
            "audio/x-vnd.audioexplosion.mjuicemediafile": ".mjf",
            "video/x-motion-jpeg": ".mjpg",
            "application/base64": ".mm",
            "application/x-meme": ".mm",
            "application/base64.copy": ".mme",
            "audio/mod": ".mod",
            "audio/x-mod": ".mod",
            "video/quicktime": ".moov",
            "video/quicktime.copy": ".qt",
            "video/x-sgi-movie": ".movie",
            "audio/mpeg.copy": ".mpga",
            "audio/x-mpeg": ".mp2",
            "video/x-mpeg": ".mp2",
            "video/x-mpeq2a": ".mp2",
            "audio/mpeg3": ".mp3",
            "audio/x-mpeg-3": ".mp3",
            "video/x-mpeg.copy": ".mp3",
            "application/x-project": ".mpc",
            "application/vnd.ms-project": ".mpp",
            "application/x-project.copy": ".mpx",
            "application/marc": ".mrc",
            "application/x-troff-ms": ".ms",
            "video/x-sgi-movie.copy": ".mv",
            "audio/make.copy": ".pfunk",
            "application/x-vnd.audioexplosion.mzz": ".mzz",
            "image/naplps": ".nap",
            "image/naplps.copy": ".naplps",
            "application/x-netcdf.copy": ".nc",
            "application/vnd.nokia.configuration-message": ".ncm",
            "image/x-niff": ".nif",
            "image/x-niff.copy": ".niff",
            "application/x-mix-transfer": ".nix",
            "application/x-conference": ".nsc",
            "application/x-navidoc": ".nvd",
            "application/oda": ".oda",
            "application/x-omc": ".omc",
            "application/x-omcdatamaker": ".omcd",
            "application/x-omcregerator": ".omcr",
            "text/x-pascal": ".p",
            "application/pkcs10": ".p10",
            "application/x-pkcs10": ".p10",
            "application/pkcs-12": ".p12",
            "application/x-pkcs12": ".p12",
            "application/x-pkcs7-signature": ".p7a",
            "application/pkcs7-mime": ".p7c",
            "application/x-pkcs7-mime": ".p7c",
            "application/pkcs7-mime.copy": ".p7m",
            "application/x-pkcs7-mime.copy": ".p7m",
            "application/x-pkcs7-certreqresp": ".p7r",
            "application/pkcs7-signature": ".p7s",
            "application/pro_eng": ".part",
            "text/pascal": ".pas",
            "image/x-portable-bitmap": ".pbm",
            "application/vnd.hp-pcl": ".pcl",
            "application/x-pcl": ".pcl",
            "image/x-pict": ".pct",
            "image/x-pcx": ".pcx",
            "chemical/x-pdb": ".pdb",
            "application/pdf": ".pdf",
            "audio/make.my.funk": ".pfunk",
            "image/x-portable-graymap": ".pgm",
            "image/x-portable-greymap": ".pgm",
            "image/pict": ".pic",
            "image/pict.copy": ".pict",
            "application/x-newton-compatible-pkg": ".pkg",
            "application/vnd.ms-pki.pko": ".pko",
            "text/x-script.perl": ".pl",
            "application/x-pixclscript": ".plx",
            "image/x-xpixmap": ".pm",
            "text/x-script.perl-module": ".pm",
            "application/x-pagemaker": ".pm4",
            "application/x-pagemaker.copy": ".pm5",
            "image/png": ".png",
            "application/x-portable-anymap": ".pnm",
            "image/x-portable-anymap": ".pnm",
            "application/mspowerpoint": ".pot",
            "application/vnd.ms-powerpoint": ".pot",
            "model/x-pov": ".pov",
            "application/vnd.ms-powerpoint.copy": ".pwz",
            "image/x-portable-pixmap": ".ppm",
            "application/mspowerpoint.copy": ".ppz",
            "application/powerpoint": ".ppt",
            "application/x-mspowerpoint": ".ppt",
            "application/x-freelance": ".pre",
            "application/pro_eng.copy": ".prt",
            "paleovu/x-pv": ".pvu",
            "text/x-script.phyton": ".py",
            "application/x-bytecode.python": ".pyc",
            "audio/vnd.qcelp": ".qcp",
            "image/x-quicktime": ".qif",
            "video/x-qtc": ".qtc",
            "image/x-quicktime.copy": ".qtif",
            "audio/x-pn-realaudio": ".ra",
            "audio/x-pn-realaudio-plugin": ".ra",
            "audio/x-realaudio": ".ra",
            "audio/x-pn-realaudio.copy": ".rmp",
            "application/x-cmu-raster": ".ras",
            "image/cmu-raster": ".ras",
            "image/x-cmu-raster": ".ras",
            "image/cmu-raster.copy": ".rast",
            "text/x-script.rexx": ".rexx",
            "image/vnd.rn-realflash": ".rf",
            "image/x-rgb": ".rgb",
            "application/vnd.rn-realmedia": ".rm",
            "audio/mid": ".rmi",
            "audio/x-pn-realaudio-plugin.copy": ".rpm",
            "application/ringing-tones": ".rng",
            "application/vnd.nokia.ringing-tone": ".rng",
            "application/vnd.rn-realplayer": ".rnx",
            "application/x-troff": ".roff",
            "image/vnd.rn-realpix": ".rp",
            "text/richtext": ".rt",
            "text/vnd.rn-realtext": ".rt",
            "application/rtf": ".rtf",
            "application/x-rtf": ".rtf",
            "text/richtext.copy": ".rtx",
            "application/rtf.copy": ".rtx",
            "video/vnd.rn-realvideo": ".rv",
            "text/x-asm.copy": ".s",
            "audio/s3m": ".s3m",
            "application/x-tbook": ".sbk",
            "application/x-lotusscreencam": ".scm",
            "text/x-script.guile": ".scm",
            "text/x-script.scheme": ".scm",
            "video/x-scm": ".scm",
            "application/sdp": ".sdp",
            "application/x-sdp": ".sdp",
            "application/sounder": ".sdr",
            "application/sea": ".sea",
            "application/x-sea": ".sea",
            "application/set": ".set",
            "text/sgml": ".sgm",
            "text/x-sgml": ".sgm",
            "text/sgml.copy": ".sgml",
            "text/x-sgml.copy": ".sgml",
            "application/x-bsh.copy": ".shar",
            "application/x-sh": ".sh",
            "application/x-shar": ".sh",
            "text/x-script.sh": ".sh",
            "application/x-shar.copy": ".shar",
            "text/x-server-parsed-html": ".shtml",
            "audio/x-psid": ".sid",
            "application/x-sit": ".sit",
            "application/x-stuffit": ".sit",
            "application/x-koan": ".skd",
            "application/x-koan.copy": ".skt",
            "application/x-seelogo": ".sl",
            "application/smil": ".smi",
            "application/smil.copy": ".smil",
            "audio/basic.copy": ".snd",
            "audio/x-adpcm": ".snd",
            "application/solids": ".sol",
            "application/x-pkcs7-certificates": ".spc",
            "text/x-speech": ".spc",
            "application/futuresplash": ".spl",
            "application/x-sprite": ".spr",
            "application/x-sprite.copy": ".sprite",
            "application/x-wais-source": ".src",
            "text/x-server-parsed-html.copy": ".ssi",
            "application/streamingmedia": ".ssm",
            "application/vnd.ms-pki.certstore": ".sst",
            "application/step": ".step",
            "application/sla": ".stl",
            "application/vnd.ms-pki.stl": ".stl",
            "application/x-navistyle": ".stl",
            "application/step.copy": ".stp",
            "application/x-sv4cpio": ".sv4cpio",
            "application/x-sv4crc": ".sv4crc",
            "application/x-world": ".svr",
            "x-world/x-svr": ".svr",
            "application/x-shockwave-flash": ".swf",
            "application/x-troff.copy": ".tr",
            "text/x-speech.copy": ".talk",
            "application/x-tar": ".tar",
            "application/toolbook": ".tbk",
            "application/x-tbook.copy": ".tbk",
            "application/x-tcl": ".tcl",
            "text/x-script.tcl": ".tcl",
            "text/x-script.tcsh": ".tcsh",
            "application/x-tex": ".tex",
            "application/x-texinfo": ".texi",
            "application/x-texinfo.copy": ".texinfo",
            "application/plain": ".text",
            "application/gnutar": ".tgz",
            "application/x-compressed.copy": ".zip",
            "image/tiff": ".tif",
            "image/x-tiff": ".tif",
            "image/tiff.copy": ".tiff",
            "image/x-tiff.copy": ".tiff",
            "audio/tsp-audio": ".tsi",
            "application/dsptype": ".tsp",
            "audio/tsplayer": ".tsp",
            "text/tab-separated-values": ".tsv",
            "image/florian.copy": ".turbot",
            "text/x-uil": ".uil",
            "text/uri-list": ".uni",
            "text/uri-list.copy": ".uris",
            "application/i-deas": ".unv",
            "application/x-ustar": ".ustar",
            "multipart/x-ustar": ".ustar",
            "text/x-uuencode": ".uu",
            "text/x-uuencode.copy": ".uue",
            "application/x-cdlink": ".vcd",
            "text/x-vcalendar": ".vcs",
            "application/vda": ".vda",
            "video/vdo": ".vdo",
            "application/groupwise": ".vew",
            "video/vivo": ".viv",
            "video/vnd.vivo": ".viv",
            "video/vivo.copy": ".vivo",
            "video/vnd.vivo.copy": ".vivo",
            "application/vocaltec-media-desc": ".vmd",
            "application/vocaltec-media-file": ".vmf",
            "audio/voc": ".voc",
            "audio/x-voc": ".voc",
            "video/vosaic": ".vos",
            "audio/voxware": ".vox",
            "audio/x-twinvq-plugin": ".vqe",
            "audio/x-twinvq": ".vqf",
            "audio/x-twinvq-plugin.copy": ".vql",
            "application/x-vrml": ".vrml",
            "model/vrml": ".vrml",
            "x-world/x-vrml": ".vrml",
            "x-world/x-vrt": ".vrt",
            "application/x-visio": ".vsd",
            "application/x-visio.copy": ".vsw",
            "application/wordperfect6.0": ".w60",
            "application/wordperfect6.1": ".w61",
            "audio/wav": ".wav",
            "audio/x-wav": ".wav",
            "application/x-qpro": ".wb1",
            "image/vnd.wap.wbmp": ".wbmp",
            "application/vnd.xara": ".web",
            "application/x-123": ".wk1",
            "windows/metafile": ".wmf",
            "text/vnd.wap.wml": ".wml",
            "application/vnd.wap.wmlc": ".wmlc",
            "text/vnd.wap.wmlscript": ".wmls",
            "application/vnd.wap.wmlscriptc": ".wmlsc",
            "application/wordperfect": ".wp",
            "application/wordperfect.copy": ".wpd",
            "application/wordperfect6.0.copy": ".wp5",
            "application/x-wpwin": ".wpd",
            "application/x-lotus": ".wq1",
            "application/mswrite": ".wri",
            "application/x-wri": ".wri",
            "application/x-world.copy": ".wrl",
            "model/vrml.copy": ".wrz",
            "x-world/x-vrml.copy": ".wrz",
            "text/scriplet": ".wsc",
            "application/x-wais-source.copy": ".wsrc",
            "application/x-wintalk": ".wtk",
            "image/x-xbitmap": ".xbm",
            "image/x-xbm": ".xbm",
            "image/xbm": ".xbm",
            "video/x-amt-demorun": ".xdr",
            "xgl/drawing": ".xgz",
            "image/vnd.xiff": ".xif",
            "application/excel": ".xl",
            "application/excel.copy": ".xlw",
            "application/x-excel": ".xla",
            "application/x-msexcel": ".xla",
            "application/vnd.ms-excel": ".xlb",
            "application/x-excel.copy": ".xlw",
            "application/vnd.ms-excel.copy": ".xlw",
            "application/x-msexcel.copy": ".xlw",
            "audio/xm": ".xm",
            "application/xml": ".xml",
            "text/xml": ".xml",
            "xgl/movie": ".xmz",
            "application/x-vnd.ls-xpix": ".xpix",
            "image/x-xpixmap.copy": ".xpm",
            "image/xpm": ".xpm",
            "image/png.copy": ".x-png",
            "video/x-amt-showrun": ".xsr",
            "image/x-xwd": ".xwd",
            "image/x-xwindowdump": ".xwd",
            "chemical/x-pdb.copy": ".xyz",
            "application/x-compress": ".z",
            "application/x-zip-compressed": ".zip",
            "application/zip": ".zip",
            "multipart/x-zip": ".zip",
            "text/x-script.zsh": ".zsh",

        }
        try:
            return types.get(file_type)

        except Exception:
            return 'Type Value Error'

    def Handel_Browse(self):

        # Check Valid Link
        try:
            filename = urlp(self.lineEdit.text()).path  # Get File Name From Url
            urlpath = requests.get(self.lineEdit.text())  # Url Meta Data
            file_type = urlpath.headers['Content-Type']  # Get File Type From Url
            types = self.Handel_Types(file_type)
            if '.' in filename:  # Check File Name Is Include Type
                browse_button = QFileDialog.getSaveFileName(self, caption='Save As', directory=f'{filename}',
                                                            filter='All Files (*.*)', )
            else:  # Add File Type
                browse_button = QFileDialog.getSaveFileName(self, caption='Save As',
                                                            directory=f'{filename}{types}',
                                                            filter='All Files (*.*)', )

            self.lineEdit_2.setText(f'{browse_button[0][:]}')

        except Exception:  # Link Error
            QMessageBox.warning(self, 'Corrupted Link', 'Please Make sure you entered a valid link !')

    def Handel_Progress(self, blocknum, blocksize, totalssize):

        read = blocknum * blocksize

        if totalssize > 0:
            percent = read * 100 / totalssize
            self.progressBar.setValue(int(percent))
            QApplication.processEvents()

    def Start_Download(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()

        try:

            urreq.urlretrieve(url, save_location, self.Handel_Progress)

        except Exception:

            QMessageBox.warning(self, 'Download Error', 'The Download Filed')
            return

        QMessageBox.information(self, 'Download Completed', 'The Download Finished')

        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

    # Download File End

    def Get_Tube_Video(self):
        try:
            video_url = self.lineEdit_4.text()
            v = pafy.new(video_url)
            video_meta = v.allstreams

            for vm in video_meta:

                size = humanize.naturalsize(vm.get_filesize())  # Convert Size KB To MB
                video_data = f'{vm.mediatype} {vm.extension} {vm.quality} {size}'
                self.comboBox.addItem(video_data)
                QApplication.processEvents()

        except ValueError:
            QMessageBox.warning(self, 'Corrupted Link', 'Verify that you have entered a valid link')
            return

    def Save_browse(self):
        self.lineEdit_3.setText(QFileDialog.getExistingDirectory(self))

    def down_rate(self, rate):

        speed = ['Kbs', 'Mbs']

        if rate >= 1024.0:

            return f'{int(rate * 0.0009765625)} {speed[1]}'

        else:

            kbs = int(str(rate * 0.0009765625).split('.')[-1]).__str__()
            return f'{kbs[:3]} {speed[0]}'

    def Download_Tube_Video(self):
        try:

            save_location = self.lineEdit_3.text()
            quality = self.comboBox.currentIndex()
            video_url = self.lineEdit_4.text()

            v = pafy.new(video_url)
            vd = v.allstreams

            def progressbar(total, recvd, ratio, rate, eta):

                self.progressBar_2.setValue(int(recvd * 100 / total))
                speed_method = self.down_rate(rate)

                down_meta = humanize.naturalsize(total, binary=True, gnu=True), speed_method[0], speed_method[
                    1], humanize.naturaldelta(dt.timedelta(seconds=eta))

                self.lineEdit_7.setText(f'Size = {down_meta[0]} Speed = {speed_method} remaining time: {down_meta[-1]}')
                QApplication.processEvents()

            if save_location != '':

                vd[quality].download(filepath=save_location, quiet=True, callback=progressbar)
                self.progressBar_2.setValue(0)
                self.lineEdit_4.setText('')
                self.lineEdit_3.setText('')
                self.comboBox.addItem('')
            else:

                QMessageBox.warning(self, 'The save path is empty', 'Choose a place to save the video to')
                return

        except Exception:
            QMessageBox.warning(self, 'Corrupted Link', 'Verify that you have entered a valid link')
            return

# https://www.youtube.com/watch?v=RhGxcV7akkw


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()  # Infinite Loop


if __name__ == '__main__':
    main()
