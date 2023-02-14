import sys
import os
import time

for i in sys.argv:
   print("开始打印参数")
   print(i)

currentTime = time.strftime("%Y/%m/%d", time.localtime())
commonHeaderString = """//
//  %s
//  YW
//
//  Created by %s on """+currentTime+""".
//

"""

h_end_str = "\n\n@end\n\nNS_ASSUME_NONNULL_END"
file_prefix = "YW"
dirArray = ["Controller", "DataStore", "Dependency", "Header", "Model", "Server", "View", "ViewModel"]

def main():
   moduleName = sys.argv[1]
   print("开始创建模块:",moduleName)
   author = sys.argv[2]
#   author = getpass.getuser()
   parent_path = os.path.dirname(sys.path[0])#父路径
   print("parentP=" + os.path.dirname(sys.path[0]))
   mkDir(sys.path[0], moduleName, author)

def mkDir(path, moduleName, author):
   print("path:"+path, "moduleName:" + moduleName, "author:"+ author)
   fullPath = path + '/' + moduleName
   isExists=os.path.exists(fullPath)
   if isExists:
      print("创建模块失败，已存在该模块，不能重复创建")
      return
    
   # os.makedirs(fullPath)
   controller = file_prefix + moduleName + "Controller"#Controller
   viewModel = file_prefix + moduleName + "ViewModel"#ViewModel
   traceServer = file_prefix + moduleName + "TraceServer"#数据埋点
   dataStore = file_prefix + moduleName + "DataStore" #数据存储
   modelProtocols = file_prefix + moduleName + "Protocols" #header协议相关
   remoteAPIProtocol = file_prefix + moduleName + "RemoteAPIProtocol" #网络协议
   netServer = file_prefix + moduleName + "NetServer" #网络请求 遵循网络协议
   mockServer = file_prefix + moduleName + "MockServer" #模拟数据 遵循网络协议

   for commonDir in dirArray:

      commonFullDir = path+"/"+moduleName+"/"+commonDir # 路径 + 模块名 + 文件夹名
      os.makedirs(commonFullDir)
      fileName = file_prefix + moduleName + commonDir # 文件名(普通的根据文件夹来的名字)

      if commonDir == "Controller": #控制器
         classStr = "@class " +  viewModel + ";"
         content = "- (instancetype)initWithViewModel:(" + viewModel +" *)viewModel"
         contentHeader = content + ";"
         detailView = file_prefix + moduleName + "View"
         controllerImportStr = """
#import "%s.h"
#import "%s.h"
#import "%s.h"
""" % (viewModel, detailView, traceServer)
         propertyStr = """
@property (nonatomic, strong) %s *detailView;
@property (nonatomic, strong) %s *detailViewModel;
@property (nonatomic, strong) %s *traceServer;
        
""" % (detailView, viewModel, traceServer)
         controllerImpContentString = """ - (instancetype)initWithViewModel:(%s *)viewModel{
    self = [super init];
    if (self) {
        _detailViewModel = viewModel;
    }
    return self;
}

- (void)viewDidLoad {
    [super viewDidLoad];

    [self setupView];

    [self setupViewModel];
   
}
- (void)setupViewModel{
    self.detailView.actionResponder = self.detailViewModel;

}

- (void)setupView{
    self.detailView = [[%s alloc] initWithFrame:self.view.bounds];
    self.view = self.detailView;
}


- (%s *)traceServer{
    if (!_traceServer) {
       _traceServer = [[%s alloc] initWithDataStore:self.detailViewModel.dataStore];
    }
    return _traceServer;
}

""" % (viewModel, detailView, traceServer, traceServer)
         createHeaderFileWith(commonFullDir, fileName, author, "UIViewController", "", contentHeader,classStr)
         createImpFileWith(commonFullDir,fileName, author, controllerImpContentString, controllerImportStr, propertyStr)
      elif commonDir == "Header": #通用协议
         createProtocolFileWith(commonFullDir, modelProtocols, author)

      elif commonDir == "Server": #服务

         createProtocolFileWith(commonFullDir, remoteAPIProtocol, author)

         netServerImportStr = "#import \"%s.h\"" % (remoteAPIProtocol)
         createHeaderFileWith(commonFullDir, netServer, author, "NSObject", remoteAPIProtocol, "", netServerImportStr)
         createImpFileWith(commonFullDir, netServer, author)

         mockServerImportStr = netServerImportStr
         createHeaderFileWith(commonFullDir, mockServer, author, "NSObject", remoteAPIProtocol, "", mockServerImportStr)
         createImpFileWith(commonFullDir, mockServer, author)

         traceServerContent = "- (instancetype)initWithDataStore:(%s *)dataStore" % (dataStore)
         traceServerHeaderContent = traceServerContent + ";"
         traceServerHeaderImport = "#import \"%s\"\n"%(dataStore + ".h")
         createHeaderFileWith(commonFullDir, traceServer, author, "NSObject", "", traceServerHeaderContent, traceServerHeaderImport)

         imp_propertyStr = """
@property (nonatomic, strong) %s *dataStore;
""" % (dataStore)
         imp_content = traceServerContent + """{
    self = [super init];
    if (self) {
        _dataStore = dataStore;
    }
    return self;
}
"""
         createImpFileWith(commonFullDir, traceServer, author, imp_content, "", imp_propertyStr)

      elif commonDir == "Dependency":#依赖
         dependencyHeader = "+ (UIViewController*)create" + moduleName + "Controller"
         dependencyHeaderStr = dependencyHeader + ";\n\n"
         # viewModel = file_prefix + moduleName + "ViewModel"
         dependencyContentStr = dependencyHeader + """{
    %s *viewModel = [[%s alloc] initWithDataStore:[%s new]];;
    %s *vc = [[%s alloc] initWithViewModel:viewModel];
    return vc;
}
"""
         dependencyImportStr = "#import \"%s\"\n"%(viewModel + ".h")
         dependencyImportStr = dependencyImportStr + "#import \"%s\"\n" % (controller + ".h")
         dependencyImportStr = dependencyImportStr + "#import \"%s.h\"" % (dataStore)
         dependencyContentStr = dependencyContentStr % (viewModel, viewModel, dataStore, controller, controller)
         print("MMMM="+ dependencyContentStr)
         dependencyFactory = file_prefix + moduleName + commonDir + "Factory" #文件名 + Factory
         createHeaderFileWith(commonFullDir, dependencyFactory, author, "NSObject", "", dependencyHeaderStr)
         createImpFileWith(commonFullDir, dependencyFactory, author, dependencyContentStr, dependencyImportStr)
      elif commonDir == "View":
         createHeaderFileWith(commonFullDir, fileName, author, "UIView")
         createImpFileWith(commonFullDir, fileName, author)
      elif commonDir == "ViewModel":
         # dataStore = file_prefix + moduleName + "DataStore"
         viewModelContent = "@property (nonatomic, strong,readonly) %s *dataStore;\n" % (dataStore)
         viewModelFunc = "- (instancetype)initWithDataStore:(%s *)dataStore" % (dataStore)
         viewModelContent = viewModelContent + viewModelFunc + ";"
         viewModelImport = "#import \"%s.h\"" % (dataStore)
         viewModelPropertyStr = """
@property (nonatomic, strong) %s *dataStore;
""" % (dataStore)
         viewModelFuncImp = viewModelFunc + """{
    self = [super init];
    if (self) {
        _dataStore = dataStore;
    }
    return self;
}
         """
         createHeaderFileWith(commonFullDir, fileName, author, "NSObject", "", viewModelContent, viewModelImport)
         createImpFileWith(commonFullDir, fileName, author, viewModelFuncImp, "", viewModelPropertyStr)
      else:#其他

         createHeaderFileWith(commonFullDir, fileName, author, "NSObject")
         createImpFileWith(commonFullDir, fileName, author)

def createProtocolFileWith(fileDir, fileName, author):
   hf = open(fileDir + "/" + fileName + ".h", "w")
   import_str = "#import <Foundation/Foundation.h> \nNS_ASSUME_NONNULL_BEGIN\n\n"
   h_interface = commonHeaderString % (fileName, author)
   h_interface = h_interface + import_str + "@protocol %s <NSObject>\n\n" % (fileName)
   # h_head_str =  h_interface % (fileName, author, fileName)
   hf.write(h_interface)
   hf.write(h_end_str)
   hf.close

def createImpFileWith(fileDir, fileName, author, content="", importHeader="", propertyStr=""):
   mf = open(fileDir + "/" + fileName + ".m", "w")
   import_str = "#import \""+ fileName + ".h\"\n"
   if len(import_str) > 0:
      import_str = import_str + importHeader
   import_str = import_str + "\n\n"
   m_interface = commonHeaderString % (fileName, author) + import_str
   m_interface = m_interface + "@interface %s ()\n" % (fileName)
   m_interface = m_interface
   if len(propertyStr) > 0:
      m_interface = m_interface + propertyStr
   m_interface = m_interface + "\n@end\n\n@implementation %s\n\n" % (fileName)
   # m_head_str = m_interface % (fileName, fileName)
   mf.write(m_interface)
   if len(content) > 0:
      mf.write(content)
   m_end_str = "\n\n@end"
   mf.write(m_end_str)
   mf.close

def createHeaderFileWith(fileDir, fileName, author, extends, protocol="", content="", classStr="", importStr= ""):
   hf = open(fileDir + "/" + fileName + ".h", "w")
   import_str = "<UIKit/UIKit.h>"
   if extends == "NSObject":
      import_str = "<Foundation/Foundation.h>"
   
   import_str = "#import " + import_str
   if len(importStr) > 0:
      import_str = import_str + importStr
   import_str = import_str + "\n\n" + classStr + " \n\nNS_ASSUME_NONNULL_BEGIN\n\n"
   h_interface = commonHeaderString % (fileName, author) + import_str
   h_interface = h_interface + "@interface %s : %s" % (fileName, extends)
   if len(protocol) > 0:
      h_interface = h_interface + "<" + protocol + ">"
   h_interface = h_interface + "\n\n"
   hf.write(h_interface)
   if len(content) > 0:
      hf.write(content)
   hf.write(h_end_str)
   hf.close

main()

