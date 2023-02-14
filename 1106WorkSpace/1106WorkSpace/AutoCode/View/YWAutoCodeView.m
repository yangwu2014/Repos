//
//  YWAutoCodeView
//  YW
//
//  Created by yangwu2014 on 2023/02/14.
//

#import "YWAutoCodeView.h"


@interface YWAutoCodeView ()

@end

@implementation YWAutoCodeView


- (instancetype)initWithFrame:(CGRect)frame {
    
    self = [super initWithFrame:frame];
    if (self) {
        [self setupViews];
    }
    return self;
}

- (void)setupViews {
    
    UIButton *btn = [UIButton buttonWithType:UIButtonTypeCustom];
    [btn setTitle:@"按钮" forState:0];
    [btn addTarget:self action:@selector(buttonAction) forControlEvents:UIControlEventTouchUpInside];
    
    btn.frame = CGRectMake(0, 100, 80, 40);
    btn.backgroundColor = [UIColor blueColor];
    [self addSubview:btn];
}

- (void)buttonAction {
    //这点
    
    if(self.actionResponder && [self.actionResponder respondsToSelector:@selector(buttonClickAction)]) {
        [self.actionResponder buttonClickAction];
    }
   
}

-(void)setActionResponder:(id<YWAutoCodeActionResponder>)actionResponder {
    _actionResponder = actionResponder;
    
    _actionResponder.loadDataBlock = ^(BOOL success, id  _Nonnull data, NSString * _Nonnull msg) {
      
        if (success) {
            if(data){
                
                //只执行UI操作，比如列表的reload，
                
            }
            
        }else {
            NSLog(@"error:%@",msg);
            //只执行UI操作，比如错误页面的展示

        }
    };
    
}


@end
