//
//  ViewController.m
//  1106WorkSpace
//
//  Created by WoolYoung on 2022/11/6.
//

#import "ViewController.h"
#import <AVKit/AVKit.h>
#import "YWAutoCodeDependencyFactory.h"
#
@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    

    
    
    UIButton *btn = [UIButton buttonWithType:UIButtonTypeContactAdd];
    btn.frame = CGRectMake(75, 95, 160, 60);
    btn.backgroundColor =[UIColor lightGrayColor];
    btn.layer.cornerRadius = 5;
    btn.clipsToBounds = YES;
    [self.view addSubview:btn];
    
    [btn addTarget:self action:@selector(buttonAction) forControlEvents:UIControlEventTouchUpInside];
}


- (void)buttonAction {
    NSLog(@"%s",__func__);
    
  UIViewController *vc =  [YWAutoCodeDependencyFactory createAutoCodeController];
    vc.modalPresentationStyle = UIModalPresentationFullScreen;

    [self presentViewController:vc animated:YES completion:nil];
}

-(void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    
    NSLog(@"%s",__func__);

//    if ([[UIApplication sharedApplication] respondsToSelector:@selector(terminateWithSuccess)]) {
//        [[UIApplication sharedApplication] performSelector:@selector(suspend)];
//    }
    
//    UIViewController *vc =  [YWAutoCodeDependencyFactory createAutoCodeController];
//    vc.modalPresentationStyle = UIModalPresentationFullScreen;
//      [self presentViewController:vc animated:YES completion:nil];
}



@end
