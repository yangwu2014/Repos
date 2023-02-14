//
//  YWAutoCodeTraceServer
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import "YWAutoCodeTraceServer.h"


@interface YWAutoCodeTraceServer ()

@property (nonatomic, strong) YWAutoCodeDataStore *dataStore;

@end

@implementation YWAutoCodeTraceServer

- (instancetype)initWithDataStore:(YWAutoCodeDataStore *)dataStore{
    self = [super init];
    if (self) {
        _dataStore = dataStore;
    }
    return self;
}


@end