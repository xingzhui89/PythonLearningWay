'''
原理简介：
    在前面我们使用findContours来查找轮廓，我们需要传入一个参数，轮廓提取模式。
    我们经常设置为RETR_LIST或者RETR_TREE，效果还可以。
    但是我们没有讲过其含义。
    同时，我们得到的结果包含3个数组，第一个是图像，第二个是轮廓，第三个是层次结构。
    但是我们从来没有用过层次结构。那么层次结构是干啥用的呢？
    层级结构和轮廓提取方式之间有什么关系？
'''
'''
1、什么是层次结构
    一般情况下，我们使用findContours在图片中查找一个对象，有时候对象可能位于不同的位置。
    还有些情况，一个形状在另一个形状的内部。
    这种情况下，我们称外部的形状为父，内部的形状为子。
    按照这种方式分类，一幅图像中的所有轮廓之间就建立了父子关系。
    这样我们就可以确定一个轮廓与其他轮廓是怎么连接的，比如它是不是某个轮廓的子轮廓，或者父轮廓。
    这种关系称为组织结构。
    
    ***此处插入图片说明一下***
    外轮廓，子轮廓，父轮廓的概念。
'''

'''
2、OpenCV中层次结构
    不管层次结构是什么样的，每个轮廓都包含自己的信息：谁是父，谁是子。
    OpenCV使用一个含有四个元素的数组表示。
    [Next,Previous,First_Child,Parent]
    Next表示同一级组织结构中的下一个轮廓。
    Previous表示同一级结构中的前一个轮廓。
    First_Child表示它的第一个子轮廓。
    Parent表示它的福轮廓。
    如果一个轮廓没有父或者子，就为-1.
'''
'''
3、轮廓检索模式
    RETR_LIST，提取所有的轮廓，而不去创建任何父子关系。
        换句话说就是人人平等，属于同一级组织轮廓。
        如果不关心轮廓之间的关系，可以使用这个选择。
    
    RETR_EXTERNAL，只返回最外边的轮廓，所有的子轮廓都会被忽略掉。
    
    RETR_CCOMP，在这种模式下，会返回所有的轮廓，并将轮廓分为两级组织结构。
        
    RETR_TREE，这是最完美的一个模式，会返回所有轮廓，并且创建一个完整的组织结构列表。
    
'''
