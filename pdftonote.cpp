#include <iostream>
#include <stdio.h>  /* defines FILENAME_MAX */
#include <string>
//https://stackoverflow.com/questions/5919996/how-to-detect-reliably-mac-os-x-ios-linux-windows-in-c-preprocessor
#ifdef _WIN64
   //define something for Windows (64-bit)
   #include <windows.h>
   std::string getexepath()
   {
     char result[ MAX_PATH ];
     return std::string( result, GetModuleFileName( NULL, result, MAX_PATH ) );
   }
#elif _WIN32
   //define something for Windows (32-bit)
   #include <windows.h>
   std::string getexepath()
   {
     char result[ MAX_PATH ];
     return std::string( result, GetModuleFileName( NULL, result, MAX_PATH ) );
   }
#elif __APPLE__
    #include "TargetConditionals.h"
    #if TARGET_OS_IPHONE && TARGET_IPHONE_SIMULATOR
        // define something for simulator
    #elif TARGET_OS_IPHONE
        // define something for iphone
    #else
        #define TARGET_OS_OSX 1
        // define something for OSX
    #endif
#elif __ANDROID__
    //android
#elif __linux__ || __gnu_linux__
    // linux
    #include <limits.h>
    #include <unistd.h>
    std::string getexepath()
    {
      char result[ PATH_MAX ];
      ssize_t count = readlink( "/proc/self/exe", result, PATH_MAX );
      return std::string( result, (count > 0) ? count : 0 );
    }
#elif __unix // all unices not caught above
    // Unix
#elif __posix
    // POSIX
#endif
using namespace std;


class InputParser{
    public:
        InputParser (int &argc, char **argv){
            for (int i=1; i < argc; ++i)
                this->tokens.push_back(std::string(argv[i]));
        }
        /// @author iain
        const std::string& getCmdOption(const std::string &option) const{
            std::vector<std::string>::const_iterator itr;
            itr =  std::find(this->tokens.begin(), this->tokens.end(), option);
            if (itr != this->tokens.end() && ++itr != this->tokens.end()){
                return *itr;
            }
            static const std::string empty_string("");
            return empty_string;
        }
        /// @author iain
        bool cmdOptionExists(const std::string &option) const{
            return std::find(this->tokens.begin(), this->tokens.end(), option)
                   != this->tokens.end();
        }
    private:
        std::vector <std::string> tokens;
};

void main(int argc, char* argv[])
{
  // cl /EHsc hello.cpp
  // std::cout << argv[0] << std::endl;
  system("sudo apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev &&\
  sudo apt-get install python3.5-dev python3-numpy libtbb2 libtbb-dev &&\
  sudo apt-get install libjpeg-dev libpng-dev libtiff5-dev libjasper-dev libdc1394-22-dev libeigen3-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev sphinx-common libtbb-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenexr-dev libgstreamer-plugins-base1.0-dev libavutil-dev libavfilter-dev libavresample-dev");
  //return 0;
}

//FNENGINE
class listallfn{

}
class choosefn{
  public:

  int main(int argc, char* argv[]) // or char** argv
  {
    int fnno;
    cout << "fnno : ";
    cin >> fnno;
    cout << "run " << fnno;
    cout << " and its double is " << i*2 << ".\n";
    return 0;
  }
}
class populatefn{

}

//https://msdn.microsoft.com/en-us/library/ms235639.aspx
