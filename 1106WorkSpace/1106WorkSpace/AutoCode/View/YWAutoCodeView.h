//
//  YWAutoCodeView
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import <UIKit/UIKit.h>
#import "YWAutoCodeModelProtocols.h"
 

NS_ASSUME_NONNULL_BEGIN

@interface YWAutoCodeView : UIView

@property (nonatomic, weak) id<YWAutoCodeActionResponder> actionResponder;

@end

NS_ASSUME_NONNULL_END
