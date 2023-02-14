//
//  YWAutoCodeViewModel
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import <Foundation/Foundation.h>

#import "YWAutoCodeDataStore.h"
#import "YWAutoCodeModelProtocols.h"

NS_ASSUME_NONNULL_BEGIN

@interface YWAutoCodeViewModel : NSObject<YWAutoCodeActionResponder>

@property (nonatomic, strong,readonly) YWAutoCodeDataStore *dataStore;
- (instancetype)initWithDataStore:(YWAutoCodeDataStore *)dataStore;


/// 获取第一次数据
- (void)loadData;


/// 获取下一页数据
- (void)loadMoreData;


@end

NS_ASSUME_NONNULL_END
