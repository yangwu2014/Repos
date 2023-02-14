//
//  YWAutoCodeModelProtocols
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import <Foundation/Foundation.h> 
NS_ASSUME_NONNULL_BEGIN

@protocol YWAutoCodeModelProtocols <NSObject>

@end

@protocol YWAutoCodeActionResponder <NSObject>

typedef void(^AutoCodeLoadDataBlock)(BOOL success,id data,NSString *msg);

@property (nonatomic, copy) AutoCodeLoadDataBlock loadDataBlock;

- (void)buttonClickAction;


@end


NS_ASSUME_NONNULL_END
