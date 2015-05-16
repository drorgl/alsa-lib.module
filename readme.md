# alsa-lib GYP Module

** Experimental **

expose alsa-lib and salsa-lib through gyp

- can be used stand alone to compile alsa-lib as static/shared libraries
	static/shared library can be changed in the variables section of alsa-lib.gyp
	alsa/salsa can be changed in the variables section of alsa-lib.gyp
- can be used as part of a bigger gyp project (which was the original intent) :

- creates and copies published headers to ./include and ./include/alsa for maximum compatibility

```
'dependencies':[
	'alsa-lib.module/alsa-lib.gyp:alsa-lib'
]
```

alsa-lib source git://git.alsa-project.org/alsa-lib.git
salsa-lib source git://git.kernel.org/pub/scm/linux/kernel/git/tiwai/salsa-lib.git

I'm in no way associated with alsa.

```
gyp alsa-lib.gyp -DOS=linux -Dtarget_arch=ia32 --depth=. -f make --generator-output=./build.linux32/

gyp alsa-lib.gyp -DOS=linux -Dtarget_arch=x64 --depth=. -f make --generator-output=./build.linux64/

gyp alsa-lib.gyp -DOS=android -Dtarget_arch=arm --depth=. -f make --generator-output=./build.android/
```
