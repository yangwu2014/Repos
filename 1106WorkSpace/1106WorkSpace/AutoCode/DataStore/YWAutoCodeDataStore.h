//
//  YWAutoCodeDataStore
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import <Foundation/Foundation.h>

 

NS_ASSUME_NONNULL_BEGIN

@interface YWAutoCodeDataStore : NSObject

@property (nonatomic, strong, readonly) NSMutableArray *dataSource;

- (void)addData:(NSMutableArray *)data;
- (void)removeAllData;

@end

NS_ASSUME_NONNULL_END
