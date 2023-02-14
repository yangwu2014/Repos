//
//  YWAutoCodeController
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import "YWAutoCodeController.h"

#import "YWAutoCodeViewModel.h"
#import "YWAutoCodeView.h"
#import "YWAutoCodeTraceServer.h"


@interface YWAutoCodeController ()

@property (nonatomic, strong) YWAutoCodeView *detailView;
@property (nonatomic, strong) YWAutoCodeViewModel *detailViewModel;
@property (nonatomic, strong) YWAutoCodeTraceServer *traceServer;//埋点
        

@end

@implementation YWAutoCodeController

 - (instancetype)initWithViewModel:(YWAutoCodeViewModel *)viewModel{
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
    self.detailView = [[YWAutoCodeView alloc] initWithFrame:self.view.bounds];
    self.detailView.backgroundColor = [UIColor whiteColor];
    self.view = self.detailView;
}


- (YWAutoCodeTraceServer *)traceServer{
    if (!_traceServer) {
       _traceServer = [[YWAutoCodeTraceServer alloc] initWithDataStore:self.detailViewModel.dataStore];
    }
    return _traceServer;
}



@end
