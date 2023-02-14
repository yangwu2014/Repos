//
//  YWAutoCodeNetServer
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import <Foundation/Foundation.h>

#import "YWAutoCodeRemoteAPIProtocol.h" 

NS_ASSUME_NONNULL_BEGIN

@interface YWAutoCodeNetServer : NSObject<YWAutoCodeRemoteAPIProtocol>

- (void)requestDataWithParam:(NSDictionary *)param
                     success:(void(^)(id data))success
                     failure:(void(^)(NSString *errorMsg))failure;

@end

NS_ASSUME_NONNULL_END
