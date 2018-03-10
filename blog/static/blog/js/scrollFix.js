$.fn.scrollFix = function (opt) {
    var settings = opt;

    var $window = $(window),
        $this = $(this),
        windowHeight,
        scrollTop,
        thisHeight,
        $main = $(settings.main),
		$top = $(settings.top),
        mainHeight,
		bottomMargin = 50;
    $window.scroll(function () {
        windowHeight = $window.height();
        scrollTop = $window.scrollTop() - $top.height() - bottomMargin;
        mainHeight = $main.height();
        $this.each(function (idx, val) {
            thisHeight = $(this).height();
            // ���������߶�С�ڲ����ʱ��������
            if (mainHeight < thisHeight) {
                return false;
            }
            // ���������߶ȴ��ڲ���������¹��߶�+���ڸ߶ȴ��ڲ�����߶�ʱ���̶������
            if (scrollTop + windowHeight > thisHeight) {
                $(this).css({
                    position: 'fixed',
                    bottom: bottomMargin
                });
            } else {
                $(this).css({
                    position: 'static'
                });
            }
        });
    });

}