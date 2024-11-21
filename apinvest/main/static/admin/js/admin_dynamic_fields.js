(function($) {
    $(document).ready(function() {
        function toggleFields() {
            $('.dynamic-contentblock_set').each(function() {
                var blockType = $(this).find('select[id$="-block_type"]').val();
                var contentField = $(this).find('.form-row.field-content');
                var imageField = $(this).find('.form-row.field-image');
                var videoField = $(this).find('.form-row.field-video_url');
                var carouselInline = $(this).find('.inline-related.dynamic-carousel_set');

                if (blockType == 'carousel') {
                    contentField.hide();
                    imageField.hide();
                    videoField.hide();
                    carouselInline.show();
                } else if (blockType == 'info') {
                    contentField.show();
                    imageField.hide();
                    videoField.hide();
                    carouselInline.hide();
                } else if (blockType == 'image') {
                    contentField.hide();
                    imageField.show();
                    videoField.hide();
                    carouselInline.hide();
                } else if (blockType == 'video') {
                    contentField.hide();
                    imageField.hide();
                    videoField.show();
                    carouselInline.hide();
                } else {
                    contentField.hide();
                    imageField.hide();
                    videoField.hide();
                    carouselInline.hide();
                }
            });
        }

        $(document).on('change', 'select[id$="-block_type"]', function() {
            toggleFields();
        });

        toggleFields();
    });
})(django.jQuery);
