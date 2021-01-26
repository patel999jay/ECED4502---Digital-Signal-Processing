# **GNURadio Installation**


GNU Radio is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in hobbyist, academic and commercial environments to support both wireless communications research and real-world radio systems.

GNU Radio is licensed under the GNU General Public License (GPL) version 3 or later. All of the code is copyright of the Free Software Foundation.
If you've never touched GNU Radio before, these pages will get you started with a running installation of GNU Radio and will show you how to take your first steps with this software radio tool.

GNU Radio is supported on almost all the major platforms:

  - [**`Linux`**](https://wiki.gnuradio.org/index.php/InstallingGR) - Read this if you want to install in **Unix base systems**.
  - [**`Windows`**](http://www.gcndevelopment.com/gnuradio/index.htm) - Read this if you want to install in **Windows systems**.
  - [**`Mac`**](https://wiki.gnuradio.org/index.php/MacInstall) - Read this if you want to install in **Mac base systems**.

# **New Installation!**

## **Windows**
[Download GR 3.8 Now **`(GR 3.8.2.0 py3.9)`** ](http://www.gcndevelopment.com/gnuradio/downloads/installers/v3.8.2.1/gnuradio_3.8.2.0_win64.msi)

  - The binaries should work with: 64-bit Windows 7/8/10.
  - Has been tested on Windows 7 and Windows 10, in both a “clean” configuration and a “busy” developer environment. Windows 8 is untested.
  - The scripts were designed for a Windows 10 / MS Server 2016 environment.

## **Mac**
[Download GR 3.8 Now **`(GR 3.8.2.0 py3.9)`** ](https://github.com/ktemkin/gnuradio-for-mac-without-macports/releases/download/3.8.0.0-0/GNURadio-3.8.0.0-0.dmg)
This is the first full release in the GNURadio 3.8 series, built off of `python3` and `Qt5`. It contain most of the features of previous releases, and maintains several of the large changes from the pre-release.

  - This distribution is based on the modern `Python 3` rather than the deprecated `Python 2`.
  - The UI has been updated to use `Qt5` for qtgui; the old wxgui has been removed upstream.
  - GNUradio has changed a bunch of its internals, favoring a new format for block description. Many existing out-of-tree modules will need to be updated.

## **Python**
If in any case above installer won't work, You can natively build [GR with conda](https://wiki.gnuradio.org/index.php/CondaInstall).
### Why use conda?
  - Conda is a cross-platform package manager (supporting Linux, macOS, and Windows) that makes it easy to install GNU Radio, its dependencies, and out-of-tree modules in a self-contained environment. Conda lets you create independent environments with their own sets of packages, and those environments are separate from your system installation and other package managers. If you've struggled with installing GNU Radio by other methods, you want to use GNU Radio with other bleeding-edge software available through conda-forge, or you want to try out a new version without affecting your tried-and-true system installation, conda may be right for you! In addition to GNU Radio, there are also related software packages you can install that may be of interest.

**You can get you `3.8.2` or, very shortly, `3.9`.**

**Install GNU Radio from conda-forge (optional)**
GNU Radio on conda-forge is split into a few subpackages. Most users will be happy with the full installation provided by the gnuradio metapackage. From within your activated "gnuradio" environment (previous step), run the command:

```sh
$   conda install gnuradio
```
This will install the latest available version of GNU Radio along with the latest version of Python. If you want a specific version of the gnuradio package (get a list of possibilities from conda search gnuradio), you can specify it like
```sh
$   conda install gnuradio=3.8.2
```
If you want a specific version of Python, you can install it before gnuradio or specify them together like
```sh
$   conda install gnuradio python=3.8
```
To upgrade all non-Python packages in your environment to their latest available versions, use the upgrade command
```sh
$   conda upgrade --all
```
The gnuradio metapackage installs all of the following subpackages:
  - gnuradio-core
  - gnuradio-grc
  - gnuradio-qtgui
  - gnuradio-uhd
  - gnuradio-video-sdl
  - gnuradio-zeromq

If you don't want all of those and their dependencies, you can install the ones you'd like individually like
```sh
$ conda install gnuradio-uhd
```
to get only the core package (always a dependency) and UHD support without any GUI elements.
### **Using GNU Radio from conda**
You can use GNU Radio from a conda environment in mostly the same way that it is normally used, provided that you have activated your "gnuradio" environment (or whatever name you might give it). So from a fresh console, you'll need to run
```sh
$   conda activate gnuradio
```
and then use whatever GNU Radio scripts or programs you want, for instance
```sh
$   gnuradio-companion
```
Windows users will find that GNU Radio Companion can also be launched from the Start Menu. Running it from there will first activate the appropriate environment, so all you need to do is click the icon!

GNU Radio will have access to the Python installed into the conda environment, and not any other installation. If you need specific Python packages to use with GNU Radio, just install them into the environment using conda install. As a last resort, `pip` or manual installation (`python setup.py install`) can also be used, but these will not be managed by conda and you'll have to be careful to manage your environment.

## **Amazing Resources**


The recommended way to get started with GNU Radio is to read the [`Guided Tutorials`](https://wiki.gnuradio.org/index.php/Tutorials).
| Link | DESCRIPTION |
| ------ | ------ |
| [**`What is GNU Radio and why do I want it?`**](https://wiki.gnuradio.org/index.php/What_is_GNU_Radio%3F) | Read this if you really have no idea what this project is about.|
| [**`Installing GNU Radio`**](https://wiki.gnuradio.org/index.php/InstallingGR) | This will explain all the steps to get a working installation of GNU Radio.|
| [**`Tutorials`**](https://wiki.gnuradio.org/index.php/Tutorials) | Several tutorials for varying skill levels.|
| [**`The Comprehensive GNU Radio Archive Network (CGRAN)`**](https://www.cgran.org/) | A list of 3rd party GNU Radio apps.|
| [**`GNURadio with Pluto SDR`**](https://patel999jay.github.io/project/internal-project/) | ADM-Pluto-File-Transfer & FM Receiver PlutoSDR.|
| [**`Frequently Asked Questions`**](https://wiki.gnuradio.org/index.php/FAQ) | Check this page before asking questions on the mailing list.|
| [**`GR WindowsInstall`**](https://wiki.gnuradio.org/index.php/WindowsInstall) | Windows Installation.|
| [**`Linux`**](https://wiki.gnuradio.org/index.php/InstallingGR) | Installation in Unix base systems.|
| [**`Mac`**](https://wiki.gnuradio.org/index.php/MacInstall) | Installation in Mac base systems.|
| [**`GR with conda`**](https://wiki.gnuradio.org/index.php/CondaInstall) | Installation using conda.|

