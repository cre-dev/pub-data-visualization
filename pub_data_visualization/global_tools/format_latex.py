





def format_latex(ss):
    """
        Formats a string so that it is compatible with Latex.
 
        :param ss: The string to format
        :type ss: string
        :return: The formatted string
        :rtype: string
    """
    tt = (ss.replace('_', ' ')
            .replace('%', '\%')
            )
    return tt