[app]

# (str) Title of your application
title = Algoritmo de Roteamento

# (str) Package name
package.name = algoritmo_de_roteamento

# (str) Package domain (needed for android/ios packaging)
package.domain = org.meuprojeto

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,flask,kivymd

# (str) Custom source folders for requirements
#source.include_exts = custom_src

# (str) The path to the key used for signing your application
# (if you are not using buildozer to sign the APK)
# android.keystore = /path/to/keystore
# android.keystore_alias = my_alias

# (str) Android SDK version to use
# (36 by default, will always be updated to the latest stable version)
# android.sdk = 36

# (str) Android NDK version to use
# (21 by default)
# android.ndk = 21b

# (bool) Use different java package for each arch (can be useful to avoid crashes)
# android.arch = armeabi-v7a

# (bool) Enable android logcat
android.logcat = True

# (list) Permissions
# comma separated e.g. android.permissions = INTERNET,ACCESS_FINE_LOCATION
android.permissions = INTERNET

# (str) Android packaging backend
# android.p4a_whitelist = requirements.txt

# (bool) android: append # (default=1)
# android.p4a = True

# (str) orientation of the application
#  choices: portrait, landscape, sensor, etc.
orientation = portrait

# (list) Android additional libraries to install
# android.p4a_packages = requests

# (bool) copy libraries on build for android (useful for deployment)
# android.packaging.copy_libs = True

# (bool) Do not compact / compress the APK package
# android.packaging.no_zip = False

# (str) default icon of the application (64x64 minimum required)
# icon.filename = <filename> (64x64 minimum required)
# android.icon = icon.png

# (str) Android feature for the application
# android.add_feature = android.hardware.camera
