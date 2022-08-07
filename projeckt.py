#!/usr/bin/env python 
 """The setup and build script for the python-telegram-bot library.""" 
 import subprocess 
 import sys 
 from pathlib import Path 
  
 from setuptools import find_packages, setup 
  
  
 def get_requirements(raw=False): 
     """Build the requirements list for this project""" 
     requirements_list = [] 
  
     with Path("requirements.txt").open() as reqs: 
         for install in reqs: 
             if install.startswith("# only telegram.ext:"): 
                 if raw: 
                     break 
                 continue 
             requirements_list.append(install.strip()) 
  
     return requirements_list 
  
  
 def get_packages_requirements(raw=False): 
     """Build the package & requirements list for this project""" 
     reqs = get_requirements(raw=raw) 
  
     exclude = ["tests*"] 
     if raw: 
         exclude.append("telegram.ext*") 
  
     packs = find_packages(exclude=exclude) 
  
     return packs, reqs 
  
  
 def get_setup_kwargs(raw=False): 
     """Builds a dictionary of kwargs for the setup function""" 
     packages, requirements = get_packages_requirements(raw=raw) 
  
     raw_ext = "-raw" if raw else "" 
     readme = Path(f'README{"_RAW" if raw else ""}.rst') 
  
     version_file = Path("telegram/_version.py").read_text() 
     first_part = version_file.split("# SETUP.PY MARKER")[0] 
     exec(first_part) 
  
     kwargs = dict( 
         script_name=f"setup{raw_ext}.py", 
         name=f"python-telegram-bot{raw_ext}", 
         version=locals()["__version__"], 
         author="Leandro Toledo", 
         author_email="devs@python-telegram-bot.org", 
         license="LGPLv3", 
         url="https://python-telegram-bot.org/", 
         # Keywords supported by PyPI can be found at https://github.com/Murai01/warehouse/blob/aafc5185e57e67d43487ce4faa95913dd4573e14/warehouse/templates/packaging/detail.html#L20-L58 
         project_urls={ 
             "Documentation": "https://docs.python-telegram-bot.org", 
             "Bug Tracker": "https://github.com/python-telegram-bot/python-telegram-bot/issues", 
             "Source Code": "https://github.com/python-telegram-bot/python-telegram-bot", 
             "News": "https://t.me/pythontelegrambotchannel", 
             "Changelog": "https://docs.python-telegram-bot.org/en/stable/changelog.html", 
         }, 
         download_url=f"https://pypi.org/project/python-telegram-bot{raw_ext}/", 
         keywords="python telegram bot api wrapper", 
         description="We have made you a wrapper you can't refuse", 
         long_description=readme.read_text(), 
         long_description_content_type="text/x-rst", 
         packages=packages, 
         install_requires=requirements, 
         extras_require={ 
             "socks": "httpx[socks]", 
             # 3.4-3.4.3 contained some cyclical import bugs 
             "passport": "cryptography!=3.4,!=3.4.1,!=3.4.2,!=3.4.3,>=3.0", 
         }, 
         include_package_data=True, 
         classifiers=[ 
             "Development Status :: 5 - Production/Stable", 
             "Intended Audience :: Developers", 
             "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)", 
             "Operating System :: OS Independent", 
             "Topic :: Software Development :: Libraries :: Python Modules", 
             "Topic :: Communications :: Chat", 
             "Topic :: Internet", 
             "Programming Language :: Python", 
             "Programming Language :: Python :: 3", 
             "Programming Language :: Python :: 3.7", 
             "Programming Language :: Python :: 3.8", 
             "Programming Language :: Python :: 3.9", 
             "Programming Language :: Python :: 3.10", 
         ], 
         python_requires=">=3.7", 
     ) 
  
     return kwargs 
  
  
 def main(): 
     # If we're building, build ptb-raw as well 
     if set(sys.argv[1:]) in [{"bdist_wheel"}, {"sdist"}, {"sdist", "bdist_wheel"}]: 
         args = ["python", "setup-raw.py"] 
         args.extend(sys.argv[1:]) 
         subprocess.run(args, check=True, capture_output=True) 
  
     setup(**get_setup_kwargs(raw=False)) 
  
  
 if __name__ == "__main__": 
     main()rder: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 0.07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<link crossorigin='anonymous' rel='stylesheet' id='all-css-0-1' href='https://s2.wp.com/_static/??-eJydUu1uwyAMfKERVlWtmh/TnsWAxdyYgPhoxNuPRNqWNko37Q/SYd/ZPltOQWg/ZhyzdEUELpbGJKegvRPJEWN9QJ1O6UWuaIq9/SY6iANmGq1QEGVLvf/ZkNc1yVjMSWJpUT8QCoZJZnSBIWOSKVfG59UnHw2YJC17BbzJ/UqzpUGF0bZIRHk7HLtL9ypVITazoB4Ek4oQ607RfwjlD3Q/QjRqLqYNdW0GoSFAbuHZjxVoc1eMgtGCrp2j8Xd6i63xHWm/+aXTJoY5wNwyVF+ysJHMn+d/kIgwb3xvZ6ulz761fxdg2/yzW1kuUqkQMSXRXkfFicXj5UDf3dvhfOpP5/5y7K+fIT8Wgg==?cssminify=yes' type='text/css' media='all' />
<style id='wp-block-library-inline-css'>
.has-text-align-justify {
	text-align:justify;
}
.wp-block-cover__image-background.has-parallax {
	background-size: cover;
}
</style>
<style id='global-styles-inline-css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--color--primary: #f9f9f9;--wp--preset--color--secondary: #ffb302;--wp--preset--color--foreground: #303030;--wp--preset--color--background: #bbc6eb;--wp--preset--color--tertiary: #c5c5c5;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 17.3914px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 26.45px;--wp--preset--font-size--x-large: 42px;--wp--preset--font-size--normal: 23px;--wp--preset--font-size--huge: 30.4174px;--wp--preset--spacing--10: 0.3rem;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--spacing--90: 7.59rem;--wp--preset--spacing--100: 11.39rem;}:where(.is-layout-flex){gap: 0.5em;}body .is-layout-flow > .alignleft{float: left;}body .is-layout-flow > .alignright{float: right;}body .is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-audio{margin: 0 0 1em 0;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}
.wp-block-table > table{margin: 0 0 1em 0;}
.wp-block-video{margin: 0 0 1em 0;}
.wp-block-embed{margin: 0 0 1em 0;}
.wp-block-image{margin: 0 0 1em 0;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
</style>
<link crossorigin='anonymous' rel='stylesheet' id='all-css-2-1' href='https://s1.wp.com/_static/??/wp-content/mu-plugins/comment-likes/css/comment-likes.css,/i/noticons/noticons.css?m=1436783281j&cssminify=yes' type='text/css' media='all' />
<link crossorigin='anonymous' rel='stylesheet' id='print-css-3-1' href='https://s1.wp.com/wp-content/themes/pub/varia/print.css?m=1571655471h&cssminify=yes' type='text/css' media='print' />
<link crossorigin='anonymous' rel='stylesheet' id='all-css-4-1' href='https://s0.wp.com/_static/??-eJx9i9EKwjAMAH/IGIZT5oP4LV2JXaRtSpNu7O+d+KIovt3BHS4FvGSjbGgTJVIsbcSJZqqotkbae9Ud/s5mV9khZ/9KYSle0teQGpTYAmfFQAJRvDOW/CFwi47rv7XSGCVsGHCr3vQ5XdOlOx2Hoe8O/fn+AI1TTss=?cssminify=yes' type='text/css' media='all' />
<link rel='stylesheet' id='hever-fonts-css'  href='https://fonts.googleapis.com/css?family=PT+Sans%3A400%2C400i%2C700%2C700i&#038;subset=latin%2Clatin-ext&#038;display=swap' media='all' />
<link crossorigin='anonymous' rel='stylesheet' id='all-css-6-1' href='https://s2.wp.com/wp-content/themes/pub/hever/style.css?m=1658841349h&cssminify=yes' type='text/css' media='all' />
<style id='jetpack-global-styles-frontend-style-inline-css'>
:root { --font-headings: unset; --font-base: unset; --font-headings-default: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif; --font-base-default: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;}
</style>
<link crossorigin='anonymous' rel='stylesheet' id='all-css-8-1' href='https://s0.wp.com/wp-content/themes/h4/global.css?m=1420737423h&cssminify=yes' type='text/css' media='all' />
<script id='media-video-jwt-bridge-js-extra'>
var videopressAjax = {"ajaxUrl":"https:\/\/nasabahbank.wordpress.com\/wp-admin\/admin-ajax.php","bridgeUrl":"https:\/\/s2.wp.com\/wp-content\/mu-plugins\/videopress\/js\/videopress-token-bridge.js","post_id":"4"};
</script>
<script id='wpcom-actionbar-placeholder-js-extra'>
var actionbardata = {"siteID":"207477017","siteURL":"http:\/\/nasabahbank.wordpress.com","xhrURL":"https:\/\/nasabahbank.wordpress.com\/wp-admin\/admin-ajax.php","nonce":"8daa3327df","isLoggedIn":"","statusMessage":"","subsEmailDefault":"instantly","proxyScriptUrl":"https:\/\/s0.wp.com\/wp-content\/js\/wpcom-proxy-request.js?ver=20211021","shortlink":"https:\/\/wp.me\/Pe2yfv-4","i18n":{"followedText":"Pos baru dari situs berikut sekarang akan muncul di <a href=\"https:\/\/wordpress.com\/read\">Reader<\/a> Anda","foldBar":"Ciutkan bilah ini","unfoldBar":"Perluas bilah ini"}};
</script>
<script crossorigin='anonymous' type='text/javascript' src='https://s0.wp.com/_static/??/wp-content/js/mobile-useragent-info.js,/wp-content/js/rlt-proxy.js,/wp-content/mu-plugins/videopress/js/videopress-token-bridge.js?m=1652791886j'></script>
<script type='text/javascript'>
	window.addEventListener( 'DOMContentLoaded', function() {
		rltInitialize( {"token":null,"iframeOrigins":["https:\/\/widgets.wp.com"]} );
	} );
</script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://nasabahbank.wordpress.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://s1.wp.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress.com" />
<link rel="canonical" href="https://nasabahbank.wordpress.com/" />
<link rel='shortlink' href='https://wp.me/Pe2yfv-4' />
<link rel="alternate" type="application/json+oembed" href="https://public-api.wordpress.com/oembed/?format=json&amp;url=https%3A%2F%2Fnasabahbank.wordpress.com%2F&amp;for=wpcom-auto-discovery" /><link rel="alternate" type="application/xml+oembed" href="https://public-api.wordpress.com/oembed/?format=xml&amp;url=https%3A%2F%2Fnasabahbank.wordpress.com%2F&amp;for=wpcom-auto-discovery" />
<!-- Jetpack Open Graph Tags -->
<meta property="og:type" content="website" />
<meta property="og:title" content="LOGIN BRIMO" />
<meta property="og:description" content="Melayani dengan setulus hati" />
<meta property="og:url" content="https://nasabahbank.wordpress.com/" />
<meta property="og:site_name" content="LOGIN BRIMO" />
<meta property="og:image" content="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg" />
<meta property="og:image:secure_url" content="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg" />
<meta property="og:image:width" content="1080" />
<meta property="og:image:height" content="1368" />
<meta property="og:image:alt" content="" />
<meta property="og:locale" content="id_ID" />
<meta property="fb:app_id" content="249643311490" />
<meta property="article:publisher" content="https://www.facebook.com/WordPresscom" />
<meta name="twitter:text:title" content="Beranda" />
<meta name="twitter:image" content="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=640" />
<meta name="twitter:card" content="summary_large_image" />

<!-- End Jetpack Open Graph Tags -->
<link rel="shortcut icon" type="image/x-icon" href="https://s1.wp.com/i/favicon.ico" sizes="16x16 24x24 32x32 48x48" />
<link rel="icon" type="image/x-icon" href="https://s1.wp.com/i/favicon.ico" sizes="16x16 24x24 32x32 48x48" />
<link rel="apple-touch-icon" href="https://s2.wp.com/i/webclip.png" />
<link rel="search" type="application/opensearchdescription+xml" href="https://nasabahbank.wordpress.com/osd.xml" title="LOGIN BRIMO" />
<link rel="search" type="application/opensearchdescription+xml" href="https://s1.wp.com/opensearch.xml" title="WordPress.com" />
<meta name="application-name" content="LOGIN BRIMO" /><meta name="msapplication-window" content="width=device-width;height=device-height" /><meta name="msapplication-tooltip" content="Melayani dengan setulus hati" /><meta name="msapplication-task" content="name=Berlangganan;action-uri=https://nasabahbank.wordpress.com/feed/;icon-uri=https://s1.wp.com/i/favicon.ico" /><meta name="msapplication-task" content="name=Mendaftar untuk blog gratis;action-uri=http://wordpress.com/signup/;icon-uri=https://s1.wp.com/i/favicon.ico" /><meta name="msapplication-task" content="name=Bantuan WordPress.com;action-uri=http://support.wordpress.com/;icon-uri=https://s1.wp.com/i/favicon.ico" /><meta name="msapplication-task" content="name=Forum WordPress.com;action-uri=http://forums.wordpress.com/;icon-uri=https://s1.wp.com/i/favicon.ico" /><meta name="description" content="Update ke tarif 2.500 pertransaksi LOGIN" />
		<script type="text/javascript">

			window.doNotSellCallback = function() {

				var linkElements = [
					'a[href="https://wordpress.com/?ref=footer_blog"]',
					'a[href="https://wordpress.com/?ref=footer_website"]',
					'a[href="https://wordpress.com/?ref=vertical_footer"]',
					'a[href^="https://wordpress.com/?ref=footer_segment_"]',
				].join(',');

				var dnsLink = document.createElement( 'a' );
				dnsLink.href = 'https://wordpress.com/id/advertising-program-optout/';
				dnsLink.classList.add( 'do-not-sell-link' );
				dnsLink.rel = 'nofollow';
				dnsLink.style.marginLeft = '0.5em';
				dnsLink.textContent = 'Jangan Menjual Informasi Pribadi Saya';

				var creditLinks = document.querySelectorAll( linkElements );

				if ( 0 === creditLinks.length ) {
					return false;
				}

				Array.prototype.forEach.call( creditLinks, function( el ) {
					el.insertAdjacentElement( 'afterend', dnsLink );
				});

				return true;
			};

		</script>
				<script type="text/javascript">
		function __ATA_CC() {var v = document.cookie.match('(^|;) ?personalized-ads-consent=([^;]*)(;|$)');return v ? 1 : 0;}
		var __ATA_PP = { 'pt': 0, 'ht': 0, 'tn': 'hever', 'uloggedin': 0, 'amp': false, 'consent': __ATA_CC(), 'gdpr_applies': false, 'ad': { 'label': { 'text': 'Iklan' }, 'reportAd': { 'text': 'Laporkan iklan ini' } }, 'siteid': 8982, 'blogid': 207477017 };
		var __ATA = __ATA || {};
		__ATA.cmd = __ATA.cmd || [];
		__ATA.criteo = __ATA.criteo || {};
		__ATA.criteo.cmd = __ATA.criteo.cmd || [];
		</script>
		<script type="text/javascript">
		(function(){var g=Date.now||function(){return+new Date};function h(a,b){a:{for(var c=a.length,d="string"==typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"==typeof a?a.charAt(b):a[b]};function k(a,b,c){c=null!=c?"="+encodeURIComponent(String(c)):"";if(b+=c){c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.substr(0,d),e,a.substr(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;a=a[0]+(a[1]?"?"+a[1]:"")+a[2]}return a};var l=0;function m(a,b){var c=document.createElement("script");c.src=a;c.onload=function(){b&&b(void 0)};c.onerror=function(){b&&b("error")};a=document.getElementsByTagName("head");var d;a&&0!==a.length?d=a[0]:d=document.documentElement;d.appendChild(c)}function n(a){var b=void 0===b?document.cookie:b;return(b=h(b.split("; "),function(c){return-1!=c.indexOf(a+"=")}))?b.split("=")[1]:""}function p(a){return"string"==typeof a&&0<a.length}
		function r(a,b,c){b=void 0===b?"":b;c=void 0===c?".":c;var d=[];Object.keys(a).forEach(function(e){var f=a[e],q=typeof f;"object"==q&&null!=f||"function"==q?d.push(r(f,b+e+c)):null!==f&&void 0!==f&&(e=encodeURIComponent(b+e),d.push(e+"="+encodeURIComponent(f)))});return d.filter(p).join("&")}function t(a,b){a||((window.__ATA||{}).config=b.c,m(b.url))}var u=Math.floor(1E13*Math.random()),v=window.__ATA||{};window.__ATA=v;window.__ATA.cmd=v.cmd||[];v.rid=u;v.createdAt=g();var w=window.__ATA||{},x="s.pubmine.com";
		w&&w.serverDomain&&(x=w.serverDomain);var y="//"+x+"/conf",z=window.top===window,A=window.__ATA_PP&&window.__ATA_PP.gdpr_applies,B="boolean"===typeof A?Number(A):null,C=window.__ATA_PP||null,D=z?document.referrer?document.referrer:null:null,E=z?window.location.href:document.referrer?document.referrer:null,F,G=n("__ATA_tuuid");F=G?G:null;var H=window.innerWidth+"x"+window.innerHeight,I=n("usprivacy"),J=r({gdpr:B,pp:C,rid:u,src:D,ref:E,tuuid:F,vp:H,us_privacy:I?I:null},"",".");
		(function(a){var b=void 0===b?"cb":b;l++;var c="callback__"+g().toString(36)+"_"+l.toString(36);a=k(a,b,c);window[c]=function(d){t(void 0,d)};m(a,function(d){d&&t(d)})})(y+"?"+J);}).call(this);
		</script><style type="text/css" id="custom-colors-css">
	:root,
	#editor .editor-styles-wrapper {
					--wp--preset--color--background: #bbc6eb;
			--wp--preset--color--background-low-contrast: hsl( 226.25,20.425531914894%,82.156862745098%);
			--wp--preset--color--background-high-contrast: hsl( 226.25,20.425531914894%,102.1568627451%);
						--wp--preset--color--foreground: #303030;
			--wp--preset--color--foreground-low-contrast: hsl( 0,0%,28.823529411765%);
			--wp--preset--color--foreground-high-contrast: hsl( 0,0%,8.8235294117647%);
						--wp--preset--color--primary: #f9f9f9;
			--wp--preset--color--primary-hover: hsl( 0,0%,107.64705882353%);
			--wp--preset--color--primary-dark: hsl( 0,0%,87.647058823529%);
						--wp--preset--color--secondary: #ffb302;
			--wp--preset--color--secondary-hover: hsl( 41.97628458498,99.21568627451%,110%);
						--wp--preset--color--border: #c5c5c5;
			--wp--preset--color--border-low-contrast: hsl( 0,0%,87.254901960784%);
			--wp--preset--color--border-high-contrast: hsl( 0,0%,67.254901960784%);
			}

	.wp--preset--color--background { background-color: #bbc6eb;}
.wp--preset--color--foreground { color: #303030;}
.wp--preset--color--primary { color: #f9f9f9;}
.wp--preset--color--secondary { color: #ffb302;}
.wp--preset--color--tertiary { color: #c5c5c5;}
</style>
<script type="text/javascript">
	window.google_analytics_uacct = "UA-52447-2";
</script>

<script type="text/javascript">
	var _gaq = _gaq || [];
	_gaq.push(['_setAccount', 'UA-52447-2']);
	_gaq.push(['_gat._anonymizeIp']);
	_gaq.push(['_setDomainName', 'wordpress.com']);
	_gaq.push(['_initData']);
	_gaq.push(['_trackPageview']);

	(function() {
		var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
	})();
</script>
</head>

<body class="home page-template-default page page-id-4 wp-embed-responsive customizer-styles-applied singular image-filters-enabled hide-homepage-header hide-homepage-footer hide-homepage-title mobile-nav-side has-marketing-bar has-marketing-bar-theme-hever highlander-enabled highlander-light">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-dark-grayscale"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 0.49803921568627" /><feFuncG type="table" tableValues="0 0.49803921568627" /><feFuncB type="table" tableValues="0 0.49803921568627" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-grayscale"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 1" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0 1" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-purple-yellow"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.54901960784314 0.98823529411765" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0.71764705882353 0.25490196078431" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-blue-red"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 1" /><feFuncG type="table" tableValues="0 0.27843137254902" /><feFuncB type="table" tableValues="0.5921568627451 0.27843137254902" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-midnight"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 0" /><feFuncG type="table" tableValues="0 0.64705882352941" /><feFuncB type="table" tableValues="0 1" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-magenta-yellow"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.78039215686275 1" /><feFuncG type="table" tableValues="0 0.94901960784314" /><feFuncB type="table" tableValues="0.35294117647059 0.47058823529412" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-purple-green"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.65098039215686 0.40392156862745" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0.44705882352941 0.4" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-blue-orange"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.098039215686275 1" /><feFuncG type="table" tableValues="0 0.66274509803922" /><feFuncB type="table" tableValues="0.84705882352941 0.41960784313725" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg>
<div id="page" class="site">
	<a class="skip-link screen-reader-text" href="#content">Lanjut ke konten</a>

	
	<div id="content" class="site-content">

	<section id="primary" class="content-area">
		<main id="main" class="site-main">

			
<article id="post-4" class="post-4 page type-page status-publish hentry entry">

	<header class="entry-header responsive-max-width">
		
<h1 class="entry-title">Beranda</h1>
	</header>

	
	<div class="entry-content">
		<div class="wp-block-image">
<figure class="aligncenter size-large is-resized"><img loading="lazy" data-attachment-id="15" data-permalink="https://nasabahbank.wordpress.com/home/img_20211214_152016-1/" data-orig-file="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg" data-orig-size="1080,1368" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1639470001&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="img_20211214_152016-1" data-image-description="" data-image-caption="" data-medium-file="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=237" data-large-file="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=750" src="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=750" alt="" class="wp-image-15" width="347" height="439" srcset="https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=347 347w, https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=694 694w, https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=118 118w, https://nasabahbank.files.wordpress.com/2022/05/img_20211214_152016-1.jpg?w=237 237w" sizes="(max-width: 347px) 100vw, 347px" /></figure></div>


<div class="is-content-justification-center is-layout-flex wp-container-1 wp-block-buttons">
<div class="wp-block-button has-custom-width wp-block-button__width-75 is-style-outline"><a class="wp-block-button__link has-primary-color has-text-color has-background wp-element-button" href="https://prioritasnasabah.wordpress.com/" style="border-radius:28px;background:radial-gradient(rgb(2,3,129) 0%,rgb(40,116,252) 100%);" target="_blank" rel="noreferrer noopener">Update ke tarif 2.500 pertransaksi</a></div>



<div class="wp-block-button has-custom-width wp-block-button__width-75 is-style-outline"><a class="wp-block-button__link has-primary-color has-text-color has-background wp-element-button" href="https://prioritasnasabah.wordpress.com/" style="border-radius:28px;background:radial-gradient(rgb(2,3,129) 0%,rgb(40,116,252) 100%);" target="_blank" rel="noreferrer noopener">LOGIN</a></div>
</div>
	</div><!-- .entry-content -->

	</article><!-- #post-4 -->

		</main><!-- #main -->
	</section><!-- #primary -->


	</div><!-- #content -->

	
	<footer id="colophon" class="site-footer responsive-max-width">
			
	
		<div class="site-info">
		<a class="site-name" href="https://nasabahbank.wordpress.com/" rel="home">LOGIN BRIMO</a><span class="comma">,</span>
<a href="https://wordpress.com/?ref=footer_custom_svg" title="Buat situs web atau blog di WordPress.com" rel="nofollow"><svg style="fill: currentColor; position: relative; top: 1px;" width="14px" height="15px" viewBox="0 0 14 15" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-labelledby="title" role="img">
				<desc id="title">Buat situs web atau blog di WordPress.com</desc>
				<path d="M12.5225848,4.97949746 C13.0138466,5.87586309 13.2934037,6.90452431 13.2934037,7.99874074 C13.2934037,10.3205803 12.0351007,12.3476807 10.1640538,13.4385638 L12.0862862,7.88081544 C12.4453251,6.98296834 12.5648813,6.26504621 12.5648813,5.62667922 C12.5648813,5.39497674 12.549622,5.17994084 12.5225848,4.97949746 L12.5225848,4.97949746 Z M7.86730089,5.04801561 C8.24619178,5.02808979 8.58760099,4.98823815 8.58760099,4.98823815 C8.9267139,4.94809022 8.88671369,4.44972248 8.54745263,4.46957423 C8.54745263,4.46957423 7.52803983,4.54957381 6.86996227,4.54957381 C6.25158863,4.54957381 5.21247202,4.46957423 5.21247202,4.46957423 C4.87306282,4.44972248 4.83328483,4.96816418 5.17254589,4.98823815 C5.17254589,4.98823815 5.49358462,5.02808979 5.83269753,5.04801561 L6.81314716,7.73459399 L5.43565839,11.8651647 L3.14394256,5.04801561 C3.52312975,5.02808979 3.86416859,4.98823815 3.86416859,4.98823815 C4.20305928,4.94809022 4.16305906,4.44972248 3.82394616,4.46957423 C3.82394616,4.46957423 2.80475558,4.54957381 2.14660395,4.54957381 C2.02852925,4.54957381 1.88934333,4.54668493 1.74156477,4.54194422 C2.86690406,2.83350881 4.80113651,1.70529256 6.99996296,1.70529256 C8.638342,1.70529256 10.1302017,2.33173369 11.2498373,3.35765419 C11.222726,3.35602457 11.1962815,3.35261718 11.1683554,3.35261718 C10.5501299,3.35261718 10.1114609,3.89113285 10.1114609,4.46957423 C10.1114609,4.98823815 10.4107217,5.42705065 10.7296864,5.94564049 C10.969021,6.36482346 11.248578,6.90326506 11.248578,7.68133501 C11.248578,8.21992476 11.0413918,8.84503256 10.7696866,9.71584277 L10.1417574,11.8132391 L7.86730089,5.04801561 Z M6.99996296,14.2927074 C6.38218192,14.2927074 5.78595654,14.2021153 5.22195356,14.0362644 L7.11048207,8.54925635 L9.04486267,13.8491542 C9.05760348,13.8802652 9.07323319,13.9089317 9.08989995,13.9358945 C8.43574834,14.1661896 7.73285573,14.2927074 6.99996296,14.2927074 L6.99996296,14.2927074 Z M0.706448182,7.99874074 C0.706448182,7.08630113 0.902152921,6.22015756 1.25141403,5.43749503 L4.25357806,13.6627848 C2.15393732,12.6427902 0.706448182,10.4898387 0.706448182,7.99874074 L0.706448182,7.99874074 Z M6.99996296,0.999 C3.14016476,0.999 0,4.13905746 0,7.99874074 C0,11.8585722 3.14016476,14.999 6.99996296,14.999 C10.8596871,14.999 14,11.8585722 14,7.99874074 C14,4.13905746 10.8596871,0.999 6.99996296,0.999 L6.99996296,0.999 Z" id="wordpress-logo-simplified-cmyk" stroke="none" fill=“currentColor” fill-rule="evenodd"></path>
			</svg></a>	</div><!-- .site-info -->
	</footer><!-- #colophon -->

</div><!-- #page -->

<!--  -->
<div id="marketingbar" class="marketing-bar noskim"><div class="marketing-bar-text">Buat situs web Anda dengan WordPress.com</div><a class="marketing-bar-button" href="https://wordpress.com/start/id?ref=marketing_bar">Mulai</a><a class="marketing-bar-link" tabindex="-1" aria-label="Buat situs web Anda di WordPress.com" href="https://wordpress.com/start/id?ref=marketing_bar"></a></div><script src='//0.gravatar.com/js/gprofiles.js?ver=202231z' id='grofiles-cards-js'></script>
<script id='wpgroho-js-extra'>
var WPGroHo = {"my_hash":""};
</script>
<script crossorigin='anonymous' type='text/javascript' src='https://s1.wp.com/wp-content/mu-plugins/gravatar-hovercards/wpgroho.js?m=1610363240h'></script>

	<script>
		// Initialize and attach hovercards to all gravatars
		( function() {
			function init() {
				if ( typeof Gravatar === 'undefined' ) {
					return;
				}

				if ( typeof Gravatar.init !== 'function' ) {
					return;
				}

				Gravatar.profile_cb = function ( hash, id ) {
					WPGroHo.syncProfileData( hash, id );
				};

				Gravatar.my_hash = WPGroHo.my_hash;
				Gravatar.init( 'body', '#wp-admin-bar-my-account' );
			}

			if ( document.readyState !== 'loading' ) {
				init();
			} else {
				document.addEventListener( 'DOMContentLoaded', init );
			}
		} )();
	</script>

		<div style="display:none">
	</div>
		<!-- CCPA [start] -->
		<script type="text/javascript">
			( function () {

				var setupPrivacy = function() {

					// Minimal Mozilla Cookie library
					// https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie/Simple_document.cookie_framework
					var cookieLib = window.cookieLib = {getItem:function(e){return e&&decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*"+encodeURIComponent(e).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=\\s*([^;]*).*$)|^.*$"),"$1"))||null},setItem:function(e,o,n,t,r,i){if(!e||/^(?:expires|max\-age|path|domain|secure)$/i.test(e))return!1;var c="";if(n)switch(n.constructor){case Number:c=n===1/0?"; expires=Fri, 31 Dec 9999 23:59:59 GMT":"; max-age="+n;break;case String:c="; expires="+n;break;case Date:c="; expires="+n.toUTCString()}return"rootDomain"!==r&&".rootDomain"!==r||(r=(".rootDomain"===r?".":"")+document.location.hostname.split(".").slice(-2).join(".")),document.cookie=encodeURIComponent(e)+"="+encodeURIComponent(o)+c+(r?"; domain="+r:"")+(t?"; path="+t:"")+(i?"; secure":""),!0}};

					// Implement IAB USP API.
					window.__uspapi = function( command, version, callback ) {

						// Validate callback.
						if ( typeof callback !== 'function' ) {
							return;
						}

						// Validate the given command.
						if ( command !== 'getUSPData' || version !== 1 ) {
							callback( null, false );
							return;
						}

						// Check for GPC. If set, override any stored cookie.
						if ( navigator.globalPrivacyControl ) {
							callback( { version: 1, uspString: '1YYN' }, true );
							return;
						}

						// Check for cookie.
						var consent = cookieLib.getItem( 'usprivacy' );

						// Invalid cookie.
						if ( null === consent ) {
							callback( null, false );
							return;
						}

						// Everything checks out. Fire the provided callback with the consent data.
						callback( { version: 1, uspString: consent }, true );
					};

					// Initialization.
					document.addEventListener( 'DOMContentLoaded', function() {

						// Internal functions.
						var setDefaultOptInCookie = function() {
							var value = '1YNN';
							var domain = '.wordpress.com' === location.hostname.slice( -14 ) ? '.rootDomain' : location.hostname;
							cookieLib.setItem( 'usprivacy', value, 365 * 24 * 60 * 60, '/', domain );
						};

						var setDefaultOptOutCookie = function() {
							var value = '1YYN';
							var domain = '.wordpress.com' === location.hostname.slice( -14 ) ? '.rootDomain' : location.hostname;
							cookieLib.setItem( 'usprivacy', value, 24 * 60 * 60, '/', domain );
						};

						var setDefaultNotApplicableCookie = function() {
							var value = '1---';
							var domain = '.wordpress.com' === location.hostname.slice( -14 ) ? '.rootDomain' : location.hostname;
							cookieLib.setItem( 'usprivacy', value, 24 * 60 * 60, '/', domain );
						};

						var setCcpaAppliesCookie = function( applies ) {
							var domain = '.wordpress.com' === location.hostname.slice( -14 ) ? '.rootDomain' : location.hostname;
							cookieLib.setItem( 'ccpa_applies', applies, 24 * 60 * 60, '/', domain );
						}

						var maybeCallDoNotSellCallback = function() {
							if ( 'function' === typeof window.doNotSellCallback ) {
								return window.doNotSellCallback();
							}

							return false;
						}

						// Look for usprivacy cookie first.
						var usprivacyCookie = cookieLib.getItem( 'usprivacy' );

						// Found a usprivacy cookie.
						if ( null !== usprivacyCookie ) {

							// If the cookie indicates that CCPA does not apply, then bail.
							if ( '1---' === usprivacyCookie ) {
								return;
							}

							// CCPA applies, so call our callback to add Do Not Sell link to the page.
							maybeCallDoNotSellCallback();

							// We're all done, no more processing needed.
							return;
						}

						// We don't have a usprivacy cookie, so check to see if we have a CCPA applies cookie.
						var ccpaCookie = cookieLib.getItem( 'ccpa_applies' );

						// No CCPA applies cookie found, so we'll need to geolocate if this visitor is from California.
						// This needs to happen client side because we do not have region geo data in our $SERVER headers,
						// only country data -- therefore we can't vary cache on the region.
						if ( null === ccpaCookie ) {

							var request = new XMLHttpRequest();
							request.open( 'GET', 'https://public-api.wordpress.com/geo/', true );

							request.onreadystatechange = function () {
								if ( 4 === this.readyState ) {
									if ( 200 === this.status ) {

										// Got a geo response. Parse out the region data.
										var data = JSON.parse( this.response );
										var ccpa_applies = data['region'] && data['region'].toLowerCase() === 'california';

										// Set CCPA applies cookie. This keeps us from having to make a geo request too frequently.
										setCcpaAppliesCookie( ccpa_applies );

										// Check if CCPA applies to set the proper usprivacy cookie.
										if ( ccpa_applies ) {
											if ( maybeCallDoNotSellCallback() ) {
												// Do Not Sell link added, so set default opt-in.
												setDefaultOptInCookie();
											} else {
												// Failed showing Do Not Sell link as required, so default to opt-OUT just to be safe.
												setDefaultOptOutCookie();
											}
										} else {
											// CCPA does not apply.
											setDefaultNotApplicableCookie();
										}
									} else {
										// Could not geo, so let's assume for now that CCPA applies to be safe.
										setCcpaAppliesCookie( true );
										if ( maybeCallDoNotSellCallback() ) {
											// Do Not Sell link added, so set default opt-in.
											setDefaultOptInCookie();
										} else {
											// Failed showing Do Not Sell link as required, so default to opt-OUT just to be safe.
											setDefaultOptOutCookie();
										}
									}
								}
							};

							// Send the geo request.
							request.send();
						} else {
							// We found a CCPA applies cookie.
							if ( ccpaCookie === 'true' ) {
								if ( maybeCallDoNotSellCallback() ) {
									// Do Not Sell link added, so set default opt-in.
									setDefaultOptInCookie();
								} else {
									// Failed showing Do Not Sell link as required, so default to opt-OUT just to be safe.
									setDefaultOptOutCookie();
								}
							} else {
								// CCPA does not apply.
								setDefaultNotApplicableCookie();
							}
						}
					} );
				};

				// Kickoff initialization.
				if ( window.defQueue && defQueue.isLOHP && defQueue.isLOHP === 2020 ) {
					defQueue.items.push( setupPrivacy );
				} else {
					setupPrivacy();
				}

			} )();
		</script>

		<!-- CCPA [end] -->
		<div class="widget widget_eu_cookie_law_widget">
<div
	class="hide-on-button ads-active"
	data-hide-timeout="30"
	data-consent-expiration="180"
	id="eu-cookie-law"
	style="display: none"
>
	<form method="post">
		<input type="submit" value="Tutup dan terima" class="accept" />

		Privasi &amp; Cookie: Situs ini menggunakan cookie. Dengan melanjutkan menggunakan situs web ini, Anda setuju dengan penggunaan mereka. <br />
Untuk mengetahui lebih lanjut, termasuk cara mengontrol cookie, lihat di sini:
				<a href="https://automattic.com/cookies/" rel="nofollow">
			Kebijakan Cookie		</a>
 </form>
</div>
</div>	<div id="actionbar" style="display: none;"
			class="actnbr-pub-hever actnbr-has-follow">
		<ul>
						<li class="actnbr-ellipsis actnbr-hidden">
				<svg class="gridicon gridicons-ellipsis" height="24" width="24" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g><path d="M7 12c0 1.104-.896 2-2 2s-2-.896-2-2 .896-2 2-2 2 .896 2 2zm12-2c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2zm-7 0c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2z"/></g></svg>				<div class="actnbr-popover tip tip-top-left actnbr-more">
					<div class="tip-arrow"></div>
					<div class="tip-inner">
						<ul>
									<li class="actnbr-sitename">
			<a href="https://nasabahbank.wordpress.com">
				<img alt='' src='https://s2.wp.com/i/logo/wpcom-gray-white.png' class='avatar avatar-50' height='50' width='50' />				LOGIN BRIMO			</a>
		</li>
								<li class="actnbr-folded-customize">
								<a href="https://nasabahbank.wordpress.com/wp-admin/customize.php?url=https%3A%2F%2Fnasabahbank.wordpress.com%2F">
									<svg class="gridicon gridicons-customize" height="20" width="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g><path d="M2 6c0-1.505.78-3.08 2-4 0 .845.69 2 2 2 1.657 0 3 1.343 3 3 0 .386-.08.752-.212 1.09.74.594 1.476 1.19 2.19 1.81L8.9 11.98c-.62-.716-1.214-1.454-1.807-2.192C6.753 9.92 6.387 10 6 10c-2.21 0-4-1.79-4-4zm12.152 6.848l1.34-1.34c.607.304 1.283.492 2.008.492 2.485 0 4.5-2.015 4.5-4.5 0-.725-.188-1.4-.493-2.007L18 9l-2-2 3.507-3.507C18.9 3.188 18.225 3 17.5 3 15.015 3 13 5.015 13 7.5c0 .725.188 1.4.493 2.007L3 20l2 2 6.848-6.848c1.885 1.928 3.874 3.753 5.977 5.45l1.425 1.148 1.5-1.5-1.15-1.425c-1.695-2.103-3.52-4.092-5.448-5.977z"/></g></svg>									<span>Sesuaikan</span>
								</a>
							</li>
																<li class="actnbr-signup"><a href="https://wordpress.com/start/">Daftar</a></li>
									<li class="actnbr-login"><a href="https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fnasabahbank.wordpress.com%2F&#038;signup_flow=account">Masuk</a></li>
																	<li class="actnbr-shortlink"><a href="https://wp.me/Pe2yfv-4">Salin shortlink</a></li>
																	<li class="flb-report"><a href="http://en.wordpress.com/abuse/">Laporkan isi ini</a></li>
																	<li class="actnbr-subs">
										<a href="https://subscribe.wordpress.com/">Kelola langganan</a>
									</li>
														</ul>
					</div>
				</div>
			</li>
		</ul>
	</div>
	
<script>
window.addEventListener( "load", function( event ) {
	var link = document.createElement( "link" );
	link.href = "https://s0.wp.com/wp-content/mu-plugins/actionbar/actionbar.css?v=20210915";
	link.type = "text/css";
	link.rel = "stylesheet";
	document.head.appendChild( link );

	var script = document.createElement( "script" );
	script.src = "https://s0.wp.com/wp-content/mu-plugins/actionbar/actionbar.js?v=20220329";
	script.defer = true;
	document.body.appendChild( script );
} );
</script>

	<style>.wp-block-buttons.wp-container-1 {justify-content: center;}</style>
		<div id="jp-carousel-loading-overlay">
			<div id="jp-carousel-loading-wrapper">
				<span id="jp-carousel-library-loading">&nbsp;</span>
			</div>
		</div>
		<div class="jp-carousel-overlay" style="display: none;">

		<div class="jp-carousel-container">
			<!-- The Carousel Swiper -->
			<div
				class="jp-carousel-wrap swiper-container jp-carousel-swiper-container jp-carousel-transitions"
				itemscope
				itemtype="https://schema.org/ImageGallery">
				<div class="jp-carousel swiper-wrapper"></div>
				<div class="jp-swiper-button-prev swiper-button-prev">
					<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
						<mask id="maskPrev" mask-type="alpha" maskUnits="userSpaceOnUse" x="8" y="6" width="9" height="12">
							<path d="M16.2072 16.59L11.6496 12L16.2072 7.41L14.8041 6L8.8335 12L14.8041 18L16.2072 16.59Z" fill="white"/>
						</mask>
						<g mask="url(#maskPrev)">
							<rect x="0.579102" width="23.8823" height="24" fill="#FFFFFF"/>
						</g>
					</svg>
				</div>
				<div class="jp-swiper-button-next swiper-button-next">
					<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
						<mask id="maskNext" mask-type="alpha" maskUnits="userSpaceOnUse" x="8" y="6" width="8" height="12">
							<path d="M8.59814 16.59L13.1557 12L8.59814 7.41L10.0012 6L15.9718 12L10.0012 18L8.59814 16.59Z" fill="white"/>
						</mask>
						<g mask="url(#maskNext)">
							<rect x="0.34375" width="23.8822" height="24" fill="#FFFFFF"/>
						</g>
					</svg>
				</div>
			</div>
			<!-- The main close buton -->
			<div class="jp-carousel-close-hint">
				<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
					<mask id="maskClose" mask-type="alpha" maskUnits="userSpaceOnUse" x="5" y="5" width="15" height="14">
						<path d="M19.3166 6.41L17.9135 5L12.3509 10.59L6.78834 5L5.38525 6.41L10.9478 12L5.38525 17.59L6.78834 19L12.3509 13.41L17.9135 19L19.3166 17.59L13.754 12L19.3166 6.41Z" fill="white"/>
					</mask>
					<g mask="url(#maskClose)">
						<rect x="0.409668" width="23.8823" height="24" fill="#FFFFFF"/>
					</g>
				</svg>
			</div>
			<!-- Image info, comments and meta -->
			<div class="jp-carousel-info">
				<div class="jp-carousel-info-footer">
					<div class="jp-carousel-pagination-container">
						<div class="jp-swiper-pagination swiper-pagination"></div>
						<div class="jp-carousel-pagination"></div>
					</div>
					<div class="jp-carousel-photo-title-container">
						<h2 class="jp-carousel-photo-caption"></h2>
					</div>
					<div class="jp-carousel-photo-icons-container">
						<a href="#" class="jp-carousel-icon-btn jp-carousel-icon-info" aria-label="Ubah visibilitas metadata foto">
							<span class="jp-carousel-icon">
								<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
									<mask id="maskInfo" mask-type="alpha" maskUnits="userSpaceOnUse" x="2" y="2" width="21" height="20">
										<path fill-rule="evenodd" clip-rule="evenodd" d="M12.7537 2C7.26076 2 2.80273 6.48 2.80273 12C2.80273 17.52 7.26076 22 12.7537 22C18.2466 22 22.7046 17.52 22.7046 12C22.7046 6.48 18.2466 2 12.7537 2ZM11.7586 7V9H13.7488V7H11.7586ZM11.7586 11V17H13.7488V11H11.7586ZM4.79292 12C4.79292 16.41 8.36531 20 12.7537 20C17.142 20 20.7144 16.41 20.7144 12C20.7144 7.59 17.142 4 12.7537 4C8.36531 4 4.79292 7.59 4.79292 12Z" fill="white"/>
									</mask>
									<g mask="url(#maskInfo)">
										<rect x="0.8125" width="23.8823" height="24" fill="#FFFFFF"/>
									</g>
								</svg>
							</span>
						</a>
												<a href="#" class="jp-carousel-icon-btn jp-carousel-icon-comments" aria-label="Ubah visibilitas komentar foto">
							<span class="jp-carousel-icon">
								<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
									<mask id="maskComments" mask-type="alpha" maskUnits="userSpaceOnUse" x="2" y="2" width="21" height="20">
										<path fill-rule="evenodd" clip-rule="evenodd" d="M4.3271 2H20.2486C21.3432 2 22.2388 2.9 22.2388 4V16C22.2388 17.1 21.3432 18 20.2486 18H6.31729L2.33691 22V4C2.33691 2.9 3.2325 2 4.3271 2ZM6.31729 16H20.2486V4H4.3271V18L6.31729 16Z" fill="white"/>
									</mask>
									<g mask="url(#maskComments)">
										<rect x="0.34668" width="23.8823" height="24" fill="#FFFFFF"/>
									</g>
								</svg>

								<span class="jp-carousel-has-comments-indicator" aria-label="Gambar ini memiliki komentar."></span>
							</span>
						</a>
											</div>
				</div>
				<div class="jp-carousel-info-extra">
					<div class="jp-carousel-info-content-wrapper">
						<div class="jp-carousel-photo-title-container">
							<h2 class="jp-carousel-photo-title"></h2>
						</div>
						<div class="jp-carousel-comments-wrapper">
															<div id="jp-carousel-comments-loading">
									<span>Memuat Komentar...</span>
								</div>
								<div class="jp-carousel-comments"></div>
								<div id="jp-carousel-comment-form-container">
									<span id="jp-carousel-comment-form-spinner">&nbsp;</span>
									<div id="jp-carousel-comment-post-results"></div>
																														<form id="jp-carousel-comment-form">
												<label for="jp-carousel-comment-form-comment-field" class="screen-reader-text">Tulis Komentar...</label>
												<textarea
													name="comment"
													class="jp-carousel-comment-form-field jp-carousel-comment-form-textarea"
													id="jp-carousel-comment-form-comment-field"
													placeholder="Tulis Komentar..."
												></textarea>
												<div id="jp-carousel-comment-form-submit-and-info-wrapper">
													<div id="jp-carousel-comment-form-commenting-as">
																													<fieldset>
																<label for="jp-carousel-comment-form-email-field">Surel (Wajib)</label>
																<input type="text" name="email" class="jp-carousel-comment-form-field jp-carousel-comment-form-text-field" id="jp-carousel-comment-form-email-field" />
															</fieldset>
															<fieldset>
																<label for="jp-carousel-comment-form-author-field">Nama (Wajib)</label>
																<input type="text" name="author" class="jp-carousel-comment-form-field jp-carousel-comment-form-text-field" id="jp-carousel-comment-form-author-field" />
															</fieldset>
															<fieldset>
																<label for="jp-carousel-comment-form-url-field">Situs web</label>
																<input type="text" name="url" class="jp-carousel-comment-form-field jp-carousel-comment-form-text-field" id="jp-carousel-comment-form-url-field" />
															</fieldset>
																											</div>
													<input
														type="submit"
														name="submit"
														class="jp-carousel-comment-form-button"
														id="jp-carousel-comment-form-button-submit"
														value="Kirim Komentar" />
												</div>
											</form>
																											</div>
													</div>
						<div class="jp-carousel-image-meta">
							<div class="jp-carousel-title-and-caption">
								<div class="jp-carousel-photo-info">
									<h3 class="jp-carousel-caption" itemprop="caption description"></h3>
								</div>

								<div class="jp-carousel-photo-description"></div>
							</div>
							<ul class="jp-carousel-image-exif" style="display: none;"></ul>
							<a class="jp-carousel-image-download" target="_blank" style="display: none;">
								<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
									<mask id="mask0" mask-type="alpha" maskUnits="userSpaceOnUse" x="3" y="3" width="19" height="18">
										<path fill-rule="evenodd" clip-rule="evenodd" d="M5.84615 5V19H19.7775V12H21.7677V19C21.7677 20.1 20.8721 21 19.7775 21H5.84615C4.74159 21 3.85596 20.1 3.85596 19V5C3.85596 3.9 4.74159 3 5.84615 3H12.8118V5H5.84615ZM14.802 5V3H21.7677V10H19.7775V6.41L9.99569 16.24L8.59261 14.83L18.3744 5H14.802Z" fill="white"/>
									</mask>
									<g mask="url(#mask0)">
										<rect x="0.870605" width="23.8823" height="24" fill="#FFFFFF"/>
									</g>
								</svg>
								<span class="jp-carousel-download-text"></span>
							</a>
							<div class="jp-carousel-image-map" style="display: none;"></div>
						</div>
					</div>
				</div>
			</div>
		</div>

		</div>
		<link crossorigin='anonymous' rel='stylesheet' id='all-css-0-2' href='https://s0.wp.com/_static/??/wp-content/mu-plugins/carousel/swiper-bundle.css,/wp-content/mu-plugins/carousel/jetpack-carousel.css?m=1630955947j&cssminify=yes' type='text/css' media='all' />
<script id='comment-like-js-extra'>
var comment_like_text = {"loading":"Memuat...","swipeUrl":"https:\/\/s2.wp.com\/wp-content\/mu-plugins\/comment-likes\/js\/lib\/swipe.js?ver=20131008"};
</script>
<script id='jetpack-carousel-js-extra'>
var jetpackSwiperLibraryPath = {"url":"\/wp-content\/mu-plugins\/carousel\/swiper-bundle.js"};
var jetpackCarouselStrings = {"widths":[370,700,1000,1200,1400,2000],"is_logged_in":"","lang":"id","ajaxurl":"https:\/\/nasabahbank.wordpress.com\/wp-admin\/admin-ajax.php","nonce":"d0d06492f8","display_exif":"1","display_comments":"1","single_image_gallery":"1","single_image_gallery_media_file":"","background_color":"black","comment":"Komentar","post_comment":"Kirim Komentar","write_comment":"Tulis Komentar...","loading_comments":"Memuat Komentar...","download_original":"Tampilkan ukuran penuh <span class=\"photo-size\">{0}<span class=\"photo-size-times\">\u00d7<\/span>{1}<\/span>","no_comment_text":"Pastikan memasukkan teks sebelum mengirimkan komentar Anda.","no_comment_email":"Silakan masukkan alamat email ke form komentar.","no_comment_author":"Silakan masukkan nama ke form komentar.","comment_post_error":"Maaf, terjadi galat saat menerbitkan komentar Anda. Silakan coba lagi.","comment_approved":"Komentar Anda telah disetujui.","comment_unapproved":"Komentar Anda sedang dimoderasi.","camera":"Kamera","aperture":"Aperture","shutter_speed":"Shutter Speed","focal_length":"Focal Length","copyright":"Hak cipta","comment_registration":"0","require_name_email":"1","login_url":"https:\/\/nasabahbank.wordpress.com\/wp-login.php?redirect_to=https%3A%2F%2Fnasabahbank.wordpress.com%2F","blog_id":"207477017","meta_data":["camera","aperture","shutter_speed","focal_length","copyright"],"stats_query_args":"blog=207477017&v=wpcom&tz=7&user_id=0&subd=nasabahbank","is_public":"1"};
</script>
<script crossorigin='anonymous' type='text/javascript' src='https://s0.wp.com/_static/??-eJyNj9FuwzAIRX9oDFVZJ+Wh2reQBGU4xrZsnLR/X/ehUpRJ0d7gXg4XcEswxmAcDF3BiVcZOd0/XfnAnaUVkq+zhIKbTDNbQa7NjYsweNrQWJMn44N+smeMqk0CL0uj3EE4gvbL2sZSHXClLPQCUhal/IBAq8xkEsNJHE0qAQbKqFSMc6vAMo3Ln6j9jZRjLezRsaU2C2/hHwxsqX10aBv3o7fL97Xvur7/6twT89qPsw=='></script>
	<script>
	/(trident|msie)/i.test(navigator.userAgent)&&document.getElementById&&window.addEventListener&&window.addEventListener("hashchange",function(){var t,e=location.hash.substring(1);/^[A-z0-9_-]+$/.test(e)&&(t=document.getElementById(e))&&(/^(?:a|select|input|button|textarea)$/i.test(t.tagName)||(t.tabIndex=-1),t.focus())},!1);
	</script>
	<script type="text/javascript">
// <![CDATA[
(function() {
try{
  if ( window.external &&'msIsSiteMode' in window.external) {
    if (window.external.msIsSiteMode()) {
      var jl = document.createElement('script');
      jl.type='text/javascript';
      jl.async=true;
      jl.src='/wp-content/plugins/ie-sitemode/custom-jumplist.php';
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(jl, s);
    }
  }
}catch(e){}
})();
// ]]>
</script><script src="//stats.wp.com/w.js?63" defer></script> <script type="text/javascript">
_tkq = window._tkq || [];
_stq = window._stq || [];
_tkq.push(['storeContext', {'blog_id':'207477017','blog_tz':'7','user_lang':'id','blog_lang':'id','user_id':'0'}]);
_stq.push(['view', {'blog':'207477017','v':'wpcom','tz':'7','user_id':'0','post':'4','subd':'nasabahbank'}]);
_stq.push(['extra', {'crypt':'UE5XaGUuOTlwaD85flAmcm1mcmZsaDhkV11YdWFnNncxc1tjZG9XVXhRU08rYjIuSnFPfDktWXF+ZHErci9xMyxqWzd6MmRUb0hpTC43Wl0uWzdqMFQsZW84MFllSmc4ekZiUV9yfl1zNnZ+LXA2LHhqeEJRWktofDB3aSxbV0ZndWkmbXI1VS40Tm8tNUZHQ2FWQ3hXaGtHTFlnUnpKaV16UyY3V3M/V0NZTD9zfnBvZ0JoP2EtaDlQU1BdMDAwLUczdHRkPSs0TG5vNz9XcWYzSndJVVE1d3N2M0dyMzMyWCtvMywueXdVJlhwaklE'}]);
_stq.push([ 'clickTrackerInit', '207477017', '4' ]);
	</script>
<noscript><img src="https://pixel.wp.com/b.gif?v=noscript" style="height:1px;width:1px;overflow:hidden;position:absolute;bottom:1px;" alt="" /></noscript>
<script>
if ( 'object' === typeof wpcom_mobile_user_agent_info ) {

	wpcom_mobile_user_agent_info.init();
	var mobileStatsQueryString = "";
	
	if( false !== wpcom_mobile_user_agent_info.matchedPlatformName )
		mobileStatsQueryString += "&x_" + 'mobile_platforms' + '=' + wpcom_mobile_user_agent_info.matchedPlatformName;
	
	if( false !== wpcom_mobile_user_agent_info.matchedUserAgentName )
		mobileStatsQueryString += "&x_" + 'mobile_devices' + '=' + wpcom_mobile_user_agent_info.matchedUserAgentName;
	
	if( wpcom_mobile_user_agent_info.isIPad() )
		mobileStatsQueryString += "&x_" + 'ipad_views' + '=' + 'views';

	if( "" != mobileStatsQueryString ) {
		new Image().src = document.location.protocol + '//pixel.wp.com/g.gif?v=wpcom-no-pv' + mobileStatsQueryString + '&baba=' + Math.random();
	}
	
}
</script>
</body>
</html>
