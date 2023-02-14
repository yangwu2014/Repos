//
//  YWAutoCodeViewModel
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import "YWAutoCodeViewModel.h"
#import "YWAutoCodeNetServer.h"

@interface YWAutoCodeViewModel ()

@property (nonatomic, strong) YWAutoCodeDataStore *dataStore;
@property (nonatomic, strong) YWAutoCodeNetServer *netServer;
@end

@implementation YWAutoCodeViewModel

@synthesize loadDataBlock;

- (instancetype)initWithDataStore:(YWAutoCodeDataStore *)dataStore{
    self = [super init];
    if (self) {
        _dataStore = dataStore;
    }
    return self;
}


- (void)loadData {
    
    [self.netServer requestDataWithParam:@{} success:^(id  _Nonnull data) {
         
        //示例，比如增加到数据源
        [self.dataStore addData:data];
        
        if (self.loadDataBlock) {
            self.loadDataBlock(YES, data, @"");
        }
        } failure:^(NSString * _Nonnull errorMsg) {
            
        }];
    
}

- (void)loadMoreData {
    
}


#pragma mark - YWAUtoCodeViewProtocols
- (void)buttonClickAction {
    
    NSLog(@"%s",__func__);
}

- (YWAutoCodeNetServer *)netServer {
    if (!_netServer) {
        _netServer = [[YWAutoCodeNetServer alloc] init];
    }
    return _netServer;
}
         


@end
